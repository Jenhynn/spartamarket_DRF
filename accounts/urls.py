from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('', views.SignupAPIView.as_view()), # 회원가입
    path('login/', TokenObtainPairView.as_view()), # 로그인 시 토큰
    path('token/refresh/', TokenRefreshView.as_view()),
    # path('<str:username>/', views.ProfileAPIView.as_view() ), # 프로필 페이지
]
