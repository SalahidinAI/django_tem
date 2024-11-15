from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    have = models.BooleanField(default=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'{self.product_name} - {self.price}'