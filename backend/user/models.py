from django.db import models
import uuid

# Create your models here.

class User(models.Model):

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    phone = models.BigIntegerField(null=True, unique=True, verbose_name="Телефон")
    email = models.EmailField(null=True, unique=True, verbose_name="Электронный адрес пользователя")

    def __str__(self):
        return f"{self.id}"

    def __repr__(self):
        return f"{self.id}"