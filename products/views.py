from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# 데코레이터: wrapping 함수. python 기능이다.
@api_view(["GET", "POST"]) # 함수형 view에는 api_view 데코레이터가 꼭 필요하다. 다른 method 가 들어오면 405 error
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # status 생략 시 200으로 응답
        # return Response(serializer.errors, status=400) # valid 하지 않으면 # raise_exception = True와 같음


@api_view(["GET"])
def product_detail(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)