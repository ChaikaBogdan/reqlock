
from .. import models
import pytest


@pytest.mark.django_db(transaction=True)
class TestHardDelete:

    def test_standalone_soft_delete(self, organisation):
        org = organisation
        org.delete()
        assert bool(org.deleted_at)

    def test_related_soft_delete(self, organisation, project_factory):
        org = organisation
        proj = project_factory(organisation=org)
        org.delete()
        assert proj.deleted_at is None


@pytest.mark.django_db(transaction=True)
class TestSoftDelete:

    def test_standalone_hard_delete(self, organisation):
        org = organisation
        pk = org.pk
        org.hard_delete()
        assert models.Organisation.objects.filter(id=pk).first() is None

    def test_related_hard_delete(self, organisation, project_factory):
        org = organisation
        proj = project_factory(organisation=org)
        pk = proj.id
        org.hard_delete()
        assert models.Project.objects.filter(id=pk).first() is None
