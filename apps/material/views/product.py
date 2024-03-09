"""
Product view
"""
from rest_framework import viewsets

from apps.material import models
from apps.material import serializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
