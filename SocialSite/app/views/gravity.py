from rest_framework.generics import ListAPIView, CreateAPIView
from ..models import Gravity, CustomUser, Followers, Repost
from ..serializers import GravitySerializer, RepostSerializer, GravityCreateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers

class GravityListView(ListAPIView):
    serializer_class = GravitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_interests = [interest for interest in user.interests.all()]

        if user_interests:
            gravities = Gravity.objects.filter(category__in=user_interests)
        else:
            gravities = Gravity.objects.all()

        return gravities.order_by('-created_at')
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        following_users = Followers.objects.filter(followers__in=[self.request.user.id])

        for obj in serializer.data:
            reposted_by_users = []
            for user in following_users:
                custom_user = CustomUser.objects.filter(pk=user.user.id).first()
                if custom_user:
                    repost_ids = [repost.gravity.id for repost in Repost.objects.filter(user=custom_user)]
                    if obj['id'] in repost_ids:
                        reposted_by_users.append(custom_user.pk)
            obj['reposted_by'] = reposted_by_users

        return Response(serializer.data)
    

class GravityCreateView(CreateAPIView):
    serializer_class = GravityCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RepostCreateView(CreateAPIView):
    serializer_class = RepostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Repost.objects.all()

    def perform_create(self, serializer):
        gravity_id = self.kwargs['gravity_id']
        gravity = Gravity.objects.get(pk=gravity_id)

        if self.get_queryset().filter(user=self.request.user, gravity=gravity).exists():
            raise serializers.ValidationError("You have already reposted this gravity.")
        
        gravity.repost_count += 1
        gravity.save()
        serializer.save(user=self.request.user, gravity=gravity)