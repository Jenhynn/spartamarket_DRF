from django.urls import path
from . import views

app_name = "products"
urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:id>/", views.product_detail), # 상품 상세, 수정, 삭제
]