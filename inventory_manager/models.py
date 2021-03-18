from django.db import models
from django.urls import reverse


class category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, null=True)
    size = models.CharField(max_length=100)
    price = models.FloatField()
    mrp = models.FloatField()
    stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=1)


    def __str__(self):
        return self.name

    def get_addtocart_url(self):
        return reverse("addtocart",kwargs={'slug':self.id})

    def get_deletecartitem_url(self):
        return reverse("deletecartitem",kwargs={'slug':self.id})


class purchase(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price = models.FloatField()
    mrp = models.FloatField()
    qty = models.IntegerField(default=0)
    total = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class sale(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    mrp = models.FloatField()
    price = models.FloatField()
    qty = models.IntegerField(default=0)
    total = models.FloatField()
    profit=models.FloatField()
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
class cartitem(models.Model):
    item=models.ForeignKey(item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.item.name

    def get_total_item_price(self):
        return self.quantity * self.item.mrp

# Create your models here.
