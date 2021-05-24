from django.db import models
from django.utils.translation import gettext as _

from .contract import Contract

# TODO: Remove jira_ticket, testrail_case and zeplin_mockup fields
# Proposal to make CustomField name, value, type (phone, email, phone, url, plain), generic FK
# https://docs.djangoproject.com/en/3.2/ref/contrib/contenttypes/#generic-relations
# remove contract FK and make it generic
class CustomField(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    jira_ticket = models.URLField(max_length=255, null=True, blank=True)
    testrail_case = models.URLField(max_length=255, null=True, blank=True)
    zeplin_mockup = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return _('%(name)s custom fields') % {'name': self.contract.name}
