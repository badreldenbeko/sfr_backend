from rest_framework import viewsets
from .models import ErrorGroup, Error
from .serializers import ErrorGroupSerializer, ErrorSerializer


class ErrorGroupViewSet(viewsets.ModelViewSet):
    queryset = ErrorGroup.objects.all()
    serializer_class = ErrorGroupSerializer


class ErrorViewSet(viewsets.ModelViewSet):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
