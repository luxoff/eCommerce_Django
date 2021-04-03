from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)
    is_digital = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return f'{self.id} : {self.name}'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = 'images/prod_placeholder.png'
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f'{self.id} : {self.customer}'


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,
                                 null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True,
                      null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'Address: {self.address}'



