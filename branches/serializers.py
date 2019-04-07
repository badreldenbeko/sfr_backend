from rest_framework import serializers
from profiles.serializers import UserSerializer
from .models import Branch


class BranchSerializer(serializers.ModelSerializer):
    branch_manager = UserSerializer(read_only=True)

    class Meta:
        model = Branch
        fields = ('__all__')
