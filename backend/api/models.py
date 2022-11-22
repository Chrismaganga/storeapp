from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)
    image = models.FileField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return "%.2f"%(float(self.price))*9