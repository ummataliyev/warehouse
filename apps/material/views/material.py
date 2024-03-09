"""
Material view
"""
from rest_framework import viewsets

from apps.material import models
from apps.material import serializers


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = models.Material.objects.all()
    serializer_class = serializers.MaterialSerializer
