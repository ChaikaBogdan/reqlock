from django.test import TestCase
from .factories import OgranisationFactory, ProjectFactory
from django.contrib.auth.models import User
from .models import *
import pytest

@pytest.mark.django_db(transaction=True)
class TestSoftDelete:
    def test_standalone_delete(self):
        org = OgranisationFactory()
        org.delete()
        assert bool(org.deleted_at)

    def test_related_delete(self):
        org = OgranisationFactory()
        proj = ProjectFactory(organisation=org)
        org.delete()
        assert proj.deleted_at is None


@pytest.mark.django_db(transaction=True)
class TestHardDelete:
    def test_standalone_delete(self):
        org = OgranisationFactory()
        org.hard_delete()
        assert len(Organisation.objects.all())==0

    def test_related_delete(self):
        org = OgranisationFactory()
        proj = ProjectFactory(organisation=org)
        org.hard_delete()
        assert len(Project.objects.all())==0
       


        
        
    
   
        