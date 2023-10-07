from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from ..models import Followers, CustomUser
from ..serializers import FollowersSerializer

class FollowUserView(CreateAPIView):
    serializer_class = FollowersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Followers.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        follower_id = self.kwargs.get('follower_id')

        if follower_id:
            try:
                user_obj = CustomUser.objects.get(id=follower_id)
                followers_obj = Followers.objects.filter(user=user_obj)
                if (followers_obj) and (not followers_obj.filter(followers__in=[user])):
                    followers_obj[0].followers.add(user)
                elif not followers_obj:
                   followers_obj = Followers.objects.create(user=user_obj)
                   followers_obj.followers.add(user)
                else:
                   raise serializers.ValidationError("You are already following this user.") 
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User with follower_id not found.")
        else:
            raise serializers.ValidationError("follower's id is required.")

class UnfollowUserView(CreateAPIView):
    serializer_class = FollowersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Followers.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        follower_id = self.kwargs.get('follower_id')

        if follower_id:
            try:
                user_obj = CustomUser.objects.get(id=follower_id)
                followers_obj = Followers.objects.filter(user=user_obj, followers__in=[user])
                if followers_obj.exists():
                    followers_obj[0].followers.remove(user)
                else:
                    raise serializers.ValidationError("You are not following this user")
            except CustomUser.DoesNotExist:
                raise serializers.ValidationError("User with follower_id not found.")
        else:
            raise serializers.ValidationError("follower's id is required.")
