from rest_framework import serializers

from branches.serializers import BranchSerializer
from .models import System


class SystemSerializer(serializers.ModelSerializer):
    branch = BranchSerializer(read_only=True)
    class Meta:
        model = System
        fields = ('__all__')
