from django.db import models

from errors.models import ErrorGroup
from systems.models import System


def upload_location(instance, filename):
    name, ext = filename.split('.')
    Klass = str(instance.__class__.__name__)
    location = 'media/{}/{}-{}.{}'.format(Klass, instance.name, instance.code, ext)
    return location


class Product(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    error_group = models.ForeignKey(ErrorGroup, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    code = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to=upload_location, default='/product.png', blank=True, null=True)
    in_request = models.BooleanField(default=False)
    res_time = models.FloatField(blank=True, null=True, help_text='Per Hours')
    fix_time = models.FloatField(blank=True, null=True, help_text='Per Hours')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('system', 'code'),)

    def __str__(self):
        return self.name + '-' + self.code
