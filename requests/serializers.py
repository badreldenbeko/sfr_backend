from rest_framework import serializers

from errors.models import Error
from errors.serializers import ErrorSerializer
from products.models import Product
from products.serializers import ProductSerializer
from .models import Request


class RequestSerializierCreate(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    error = serializers.PrimaryKeyRelatedField(queryset=Error.objects.all())

    class Meta:
        model = Request
        fields = ('__all__')


class RequestSerializierRead(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    error = ErrorSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ('__all__')
