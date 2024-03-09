"""
Warehouse object


"""
from django.db import models

from apps.material.models import Material


class Warehouse(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    remainder = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return f"{self.material.name} - ({self.price})"
