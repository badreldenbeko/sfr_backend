from django.db import models
from datetime import timedelta, datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

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
    res_time = models.DateTimeField(blank=True, null=True)
    fix_time = models.DateTimeField(blank=True, null=True)
    snt_time = models.DateTimeField(blank=True, null=True)
    cls_time = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Ref# ' + str(self.id)

    @property
    def get_res_time(self):
        if not self.res_time and self.status == 'i':
            req_td = timedelta(hours=self.product.res_time)
            self.res_time = self.snt_time + req_td
            return self.res_time

    @property
    def get_fix_time(self):
        if not self.fix_time and self.status == 'i':
            fix_td = timedelta(hours=self.product.fix_time)
            self.fix_time = self.snt_time + fix_td
            return self.fix_time

    @property
    def get_cls_time(self):
        if not self.cls_time and self.status == 'c':
            req_td = timedelta(hours=self.product.res_time)
            fix_td = timedelta(hours=self.product.fix_time)
            self.res_time = self.snt_time + req_td
            self.fix_time = self.snt_time + fix_td
            self.cls_time = datetime.now()
            return self.cls_time

    def save(self, *args, **kwargs):
        self.res_time = self.get_res_time
        self.fix_time = self.get_fix_time
        self.cls_time = self.get_cls_time
        super(Request, self).save(*args, **kwargs)
