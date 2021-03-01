from django.db import models

from .contract import Contract


class CustomField(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    jira_ticket = models.URLField(max_length=255, null=True, blank=True)
    testrail_case = models.URLField(max_length=255, null=True, blank=True)
    zeplin_mockup = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.contract.name} custom fields'
