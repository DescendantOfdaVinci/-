from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    count_on_stock = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.title} - {self.price}'


class Purchaser(models.Model):
    name = models.CharField(max_length=20)
    purchaces = models.ManyToManyField(Product, null=True)

    def __str__(self):
        return f'{self.name}'
