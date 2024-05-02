from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class SignupAPIView(APIView):
    def post(self, request):
        data = request.data
        # username, email이 필수여야 함.
        username = data.get("username")
        email = data.get("email")
        if not username or not email:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if username == get_user_model().objects.filter(username=username).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        if email == get_user_model().objects.filter(email=email).exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        user = get_user_model().objects.create_user(
            username = username,
            email = email,
            password = data.get("password"),
            nickname = data.get("nickname"),
            birthdate = data.get("birthdate"),
        )
        return Response(
            {
                "username":user.username,
                "message": "회원가입이 완료되었습니다."
            },
            status=status.HTTP_201_CREATED)
    

class ProfileAPIView(APIView):
    def get(self, request, username):
        user = get_object_or_404(get_user_model(), username=username)
        return Response(
            {
                "username" : user.username,
                "nickname" : user.nickname,
                "email": user.email,
                "birthdate": user.birthdate,
            }
        )