from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=10000)

    def __str__(self):
        return f'Producto: {self.name} | Precio: {self.price}'
