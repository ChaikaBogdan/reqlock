from django.conf import settings
from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=255)
    homepage = models.URLField(max_length=255, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.EmailField(max_length=255, null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='+')

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='+')
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Component(models.Model):
    TYPES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('MONOLITH', 'Monolith'),
        ('LAMBDA', 'Lambda'),
        ('PRODUCER', 'Producer'),
        ('CONSUMER', 'Consumer'),
        ('BROKER', 'Broker'),
        ('QUEUE', 'Queue'),
        ('WORKER', 'Worker'),
        ('DB', 'Database'),
        ('DS', 'Data Source'),
    ]
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tech_stack = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=TYPES,
        null=True, blank=True
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contract(models.Model):
    TYPES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('DESIGN', 'Design'),
    ]
    LOCK_STATUSES = [
        ('LOCK', 'Locked'),
        ('UNLOCK', 'Unlocked'),
        ('AWAIT', 'Awaiting'),

    ]
    CONTRACT_STATUTES = [
        ('DRAFT', 'Draft'),
        ('DESIGN', 'In Design'),
        ('QA', 'QA'),
        ('DEV', 'DEV'),

    ]

    TESTS_STATUSES = [
        ('FAIL', 'Failing'),
        ('PASS', 'Passing'),
        ('FLAKY', 'Unstable'),
        ('NONE', 'None'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(
        max_length=50,
        choices=TYPES,
        null=True,
        blank=True
    )
    lock_status = models.CharField(
        max_length=50,
        choices=LOCK_STATUSES,
        default='UNLOCK',
    )
    contract_status = models.CharField(
        max_length=50,
        choices=CONTRACT_STATUTES,
        default='DRAFT',
    )
    tests_status = models.CharField(
        max_length=50,
        choices=TESTS_STATUSES,
        default='NONE',
    )

    components = models.ManyToManyField(Component, blank=True, related_name='+')

    def __str__(self):
        return self.name


class CustomField(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    jira_ticket = models.URLField(max_length=255, null=True, blank=True)
    testrail_case = models.URLField(max_length=255, null=True, blank=True)
    zeplin_mockup = models.URLField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.contract.name} custom fields'


class Review(models.Model):
    contracts = models.ManyToManyField(Contract, blank=True, related_name='+')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ROLES = [
        ('QA', 'QA'),
        ('DEV', 'Developer'),
        ('MAN', 'Manager'),
        ('DIR', 'Director'),
        ('SRE', 'SRE'),
        ('DEVOPS', 'DevOps'),
        ('DESIGN', 'Designer'),
        ('PO', 'Projects owner'),

    ]
    SIGN_STATUSES = [
        ('SIGNED', 'Signed'),
        ('AWAIT', 'Requested to sign'),
        ('REJECT', 'Reject to sign'),
        ('NAN', 'Sign not required'),
    ]
    role = models.CharField(
        max_length=50,
        choices=ROLES,
        null=True,
        blank=True
    )
    sign_status = models.CharField(
        max_length=50,
        choices=SIGN_STATUSES,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user.email} reviews'
