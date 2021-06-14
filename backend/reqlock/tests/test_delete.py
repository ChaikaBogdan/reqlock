
from .. import models
import pytest


@pytest.mark.django_db(transaction=True)
def test_standalone_soft_delete(organisation):
    org = organisation
    org.delete()
    assert bool(org.deleted_at)


@pytest.mark.django_db(transaction=True)
def test_related_soft_delete(organisation, project_factory):
    org = organisation
    proj = project_factory(organisation=org)
    org.delete()
    assert proj.deleted_at is None


@pytest.mark.django_db(transaction=True)
def test_standalone_hard_delete(organisation):
    org = organisation
    org.hard_delete()
    assert len(models.Organisation.objects.all()) == 0


@pytest.mark.django_db(transaction=True)
def test_related_hard_delete(organisation, project_factory):
    org = organisation
    _ = project_factory(organisation=org)
    org.hard_delete()
    assert len(models.Project.objects.all()) == 0
