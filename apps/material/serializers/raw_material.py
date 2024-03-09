"""
RawMaterial serializer
"""
from rest_framework import serializers

from apps.material import models


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RawMaterial
        fields = '__all__'
