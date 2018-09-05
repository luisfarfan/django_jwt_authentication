from django.db import models


class Audit(models.Model):
    date_created = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(Audit):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    products = models.ManyToManyField('Products', through='UserProducts')
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('name',)


class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    class Meta:
        ordering = ('name',)


class UserProducts(models.Model):
    user = models.ForeignKey(User, on_delete=True)
    product = models.ForeignKey(Products, on_delete=True)
    date = models.DateTimeField()
