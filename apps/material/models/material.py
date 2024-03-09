"""
Material object
"""
from django.db import models


class Material(models.Model):
    class Meta:
        db_table = 'material'

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
