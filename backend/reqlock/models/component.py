from django.conf import settings
from django.db import models
from .project import Project
from .component_type import ComponentType
from .model_mixins import SoftDeleteModel


class Component(SoftDeleteModel):

    name = models.CharField(max_length=255)
    type = models.ForeignKey(ComponentType, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
