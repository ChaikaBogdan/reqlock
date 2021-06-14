import factory
from django.contrib.auth.models import User
from . import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('username',)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('user_name')
    email = factory.Faker('email')


class OgranisationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Organisation
        django_get_or_create = ('name',)
    name = factory.Faker('company')
    owner = factory.SubFactory(UserFactory)


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Project
        django_get_or_create = ('name',)
    name = factory.Faker('company')
    owner = factory.SubFactory(UserFactory)
    organisation = factory.SubFactory(OgranisationFactory)
