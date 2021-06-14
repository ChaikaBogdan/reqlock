from pytest_factoryboy import register
from .factories import UserFactory, ProjectFactory, OrganisationFactory

register(UserFactory)
register(ProjectFactory)
register(OrganisationFactory)
