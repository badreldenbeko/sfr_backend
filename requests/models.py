from django.db import models

from errors.models import Error
from products.models import Product

STATUS_CHOICES = (
    ('o', 'Open'),
    ('i', 'In Progress'),
    ('c', 'Closed')
)


class Request(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    error = models.ForeignKey(Error, blank=True, null=True, on_delete=models.SET_NULL)
    desc = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='o')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Ref# ' + str(self.id)
