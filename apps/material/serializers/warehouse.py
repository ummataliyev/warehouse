"""
Warehouse serializer
"""
from rest_framework import serializers

from apps.material import models


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = '__all__'
