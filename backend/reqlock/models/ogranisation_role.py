from django.db import models
from .organisation import Organisation
from .model_mixins import SoftDeleteModel


class OrganisationRole(SoftDeleteModel):

    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
