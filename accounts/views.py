from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import SignupSerializer


class SignupAPIView(generics.CreateAPIView):
    User = get_user_model()
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    

# class ProfileAPIView():