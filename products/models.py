from django.db import models


class Product(models.Model):
    author = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/products/')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.author + ' ' + self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
