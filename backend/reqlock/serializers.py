from rest_framework import serializers
from django.db.models import Q
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'linked_projects']

    class LinkedProjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = ['id', 'name']

    linked_projects = LinkedProjectSerializer(many=True, required=False)

    def create(self, validated_data):
        project = Project(**validated_data)
        user = self.context['request'].user
        organisation = Organisation.objects.filter(
            Q(owner=user) | Q(members__in=[user])
        ).first()
        project.organisation = organisation
        project.owner = user
        project.save()
        return project


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
