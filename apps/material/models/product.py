"""
Product object
"""
from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'product'

    name = models.CharField(max_length=150)
    code = models.CharField(max_length=25)

    def __str__(self):
        return self.name
