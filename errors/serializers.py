from rest_framework import serializers
from .models import ErrorGroup, Error


class ErrorGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorGroup
        fields = ('__all__')


class ErrorSerializer(serializers.ModelSerializer):
    error_group = ErrorGroupSerializer(read_only=True)

    class Meta:
        model = Error
        fields = ('__all__')
