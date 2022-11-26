from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    image = models.FileField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price)*8)


    def get_discount(self):
        return "122"    

   