from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')


class User(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    balance = models.IntegerField(default=0)

    def __str__(self):
        return self.login


class Order(models.Model):
    summa = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_at = models.DateTimeField(auto_now=True)
