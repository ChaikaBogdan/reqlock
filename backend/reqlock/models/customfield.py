from django.db import models
from django.utils.translation import gettext as _

from .contract import Contract

# TODO: Add new model with FK org, with field name type CUSTOM FIELDS
# TODO: Add new model CUSTOM VALUES with FK CUSTOM FIELD and FK TO CONTRACT

class CustomField(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    jira_ticket = models.URLField(max_length=255, null=True, blank=True)
    testrail_case = models.URLField(max_length=255, null=True, blank=True)
    zeplin_mockup = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return _('%(name)s custom fields') % {'name': self.contract.name}
