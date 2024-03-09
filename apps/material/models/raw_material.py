"""
RawMaterial object
"""
from django.db import models

from apps.material.models import Product
from apps.material.models import Material


class RawMaterial(models.Model):
    class Meta:
        db_table = 'raw_material'

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.product.name} - {self.material.name} ({self.quantity})"
