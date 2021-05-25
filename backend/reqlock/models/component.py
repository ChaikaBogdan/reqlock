from django.conf import settings
from django.db import models
from .project import Project
from .component_type import ComponentType


class Component(models.Model):

    name = models.CharField(max_length=255)
    type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    components_type = models.ForeignKey(
        ComponentType, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return self.name
