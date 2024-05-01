from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.ProductListAPIView.as_view(), name="product_list"),
    path("<int:id>/", views.ProductDetailAPIView.as_view()), # 상품 상세, 수정, 삭제
]