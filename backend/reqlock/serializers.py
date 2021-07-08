from rest_framework import serializers

from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'linked_projects']

    class LinkedProjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = ['id', 'name']

    linked_projects = LinkedProjectSerializer(many=True)


class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['id', 'name']


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ['id', 'name', ]


class ContractSerializer(serializers.ModelSerializer):

    components = ComponentSerializer(many=True)

    class Meta:
        model = Component
        fields = ['id', 'name', 'components']
