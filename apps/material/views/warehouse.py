"""
Warehouse view
"""
from rest_framework import viewsets

from apps.material import models
from apps.material import serializers


class WarehouselViewSet(viewsets.ModelViewSet):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.WarehouseSerializer
