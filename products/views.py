from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer
    

class ProductListAPIView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly] 

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # status 생략 시 200으로 응답
        # return Response(serializer.errors, status=400) # valid 하지 않으면 # raise_exception = True와 같음


class ProductDetailAPIView(APIView):
    def get_object(self, id):
        return get_object_or_404(Product, id=id)
    
    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_object(id) # 기존의 product를 가져와서
        serializer = ProductSerializer(product, data=request.data, partial=True) # 그 자리에 data를 넣음 # partial을 넣으면 일부 필드만도 수정 가능
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)