from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(blank=False, max_length=85)
    quantity_in_store = models.IntegerField(blank=False, default='1')
    dealer = models.CharField(blank=False, max_length=25)
    price = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=100000)
    description = models.TextField(blank=True, null=False)

    def get_absolute_url(self):
        return reverse("sklep:product-detail", kwargs={"id": self.id})
