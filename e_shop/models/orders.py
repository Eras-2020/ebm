from django.db import models
from django.contrib.auth.models import User
from .product import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
    total = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_user(user_id):
        return Order\
            .objects\
            .filter(user=user_id)\
            .order_by('-order_date')
