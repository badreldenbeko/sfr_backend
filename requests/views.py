from rest_framework import viewsets
from .models import Request
from .serializers import RequestSerializierCreate, RequestSerializierRead


class RequestViewSetCreate(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializierCreate


class RequestViewSetRead(viewsets.ModelViewSet):
    queryset = Request.objects.all().order_by('-created')
    serializer_class = RequestSerializierRead
