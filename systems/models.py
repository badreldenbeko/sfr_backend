from django.db import models

from branches.models import Branch


class System(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('branch', 'name'),)

    def __str__(self):
        return 'Branch-' + self.branch.name + ' / ' + self.name
