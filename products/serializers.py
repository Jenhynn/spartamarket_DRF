# serializer 정의 (DRF 방식): 데이터를 특정 포맷으로 변경해주도록

from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer): # ModelForm 과 유사 
    class Meta:
        model = Product
        fields = "__all__"