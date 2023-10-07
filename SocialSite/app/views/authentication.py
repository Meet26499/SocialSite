from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework.response import Response
from ..models import CustomUser
from django.contrib.auth import authenticate, login
from ..serializers import RegistrationSerializer, LoginSerializer

class RegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    

class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = None

            if '@' in username:
                try:
                    user = CustomUser.objects.get(email=username)
                except CustomUser.DoesNotExist:
                    pass

            if user is None:
                try:
                    user = CustomUser.objects.get(phone_number=username)
                except CustomUser.DoesNotExist:
                    pass

            if user is not None:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    return Response({"message": "User logged in successfully"}, status=status.HTTP_200_OK)

            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
