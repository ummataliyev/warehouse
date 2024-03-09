"""
Material serializer
"""
from rest_framework import serializers

from apps.material import models


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'
