from django.db import models
from .organisation import Organisation


class ComponentType(models.Model):

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name
