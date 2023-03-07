from django.db import models
from apps.users.models import User
from apps.products.models import Product


class Cart(models.Model):
    class Meta(object):
        db_table = 'cart'

    user = models.ForeignKey(
        User, related_name='related_user', on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name='related_product', on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        'Quantity', blank=False, null=False
    )
    demo = models.CharField(
        'T shirt', blank=False, max_length=200
    )

    @property
    def total_price(self):
        return self.quantity * self.product.price
