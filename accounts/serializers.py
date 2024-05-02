from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class SignupSerializer(serializers.ModelSerializer):
    # nickname = serializers.CharField(max_length=15, required=True)
    # email = serializers.EmailField(required=True)
    # birthday = serializers.DateField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')
        # fields = ('username', 'nickname', 'email', 'birthday', 'password', 'password2')

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(data = validated_data)
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
        
