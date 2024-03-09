"""
Product serializer
"""
from rest_framework import serializers

from apps.material import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'
