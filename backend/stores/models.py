from django.db import models
from user.models import User

# Create your models here.


class Store(models.Model):
    class Meta:
        verbose_name_plural = "Магазины"
        verbose_name = "Магазин"

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=128, blank=True, default="", verbose_name="Название")

    def __str__(self):
        return f"{self.pk}, " f"{self.name}"
