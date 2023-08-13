from django.db import models

# Create your models here.

from stores.models import Store

class Product(models.Model):
    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Товар"

    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, verbose_name="Магазин")

    offer_id = models.CharField(max_length=255, blank=True, default="", verbose_name="Артикул товара")
    name = models.CharField(max_length=255, blank=True, default="", verbose_name="Название товара")