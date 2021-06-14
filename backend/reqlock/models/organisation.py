from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.db import models
from .custom_field import CustomField
from .model_mixins import SoftDeleteModel


class Organisation(SoftDeleteModel):

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='+')
    custom_fields = GenericRelation(CustomField)

    def __str__(self):
        return self.name
