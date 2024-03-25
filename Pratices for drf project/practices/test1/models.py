from django.db import models

class category(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
            return self.category_name

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title