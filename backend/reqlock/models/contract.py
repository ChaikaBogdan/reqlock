from django.db import models
from .component import Component
from .test_status import TestStatus
from .contract_status import ContractStatus
from .lock_status import LockStatus
from .contract_type import ContractType


class Contract(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    lock_status = models.ForeignKey(LockStatus, on_delete=models.CASCADE)
    contract_status = models.ForeignKey(
        ContractStatus, on_delete=models.CASCADE)
    tests_status = models.ForeignKey(TestStatus, on_delete=models.CASCADE)

    components = models.ManyToManyField(
        Component, blank=True, related_name='+')

    def __str__(self):
        return self.name
