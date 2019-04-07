from rest_framework import serializers

from errors.serializers import ErrorGroupSerializer
from systems.serializers import SystemSerializer
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    system = SystemSerializer(read_only=True)
    error_group = ErrorGroupSerializer(read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
