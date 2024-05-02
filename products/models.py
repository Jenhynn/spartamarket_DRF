from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    content = models.TextField()
    image = models.ImageField(blank=True) # 빈 채로 저장 가능
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name