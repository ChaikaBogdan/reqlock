from django.conf import settings
from django.db import models
from .organisation import Organisation
from .custom_field import CustomField
from django.contrib.contenttypes.fields import GenericRelation
from .model_mixins import SoftDeleteModel


class Project(SoftDeleteModel):

    name = models.CharField(max_length=255)
    custom_fields = GenericRelation(CustomField)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='+')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    linked_projects = models.ManyToManyField("self", blank=True, symmetrical=False, related_name='+')

    def __str__(self):
        return self.name
