"""
RawMaterial view
"""
from rest_framework import viewsets

from apps.material import models
from apps.material import serializers


class RawMaterialViewSet(viewsets.ModelViewSet):
    queryset = models.RawMaterial.objects.all()
    serializer_class = serializers.RawMaterialSerializer
