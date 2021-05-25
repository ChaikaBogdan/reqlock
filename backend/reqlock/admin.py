from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ["members"]

class CustomFieldInline(GenericStackedInline):
    model = CustomField
    extra = 1

class OrganisationAdmin(admin.ModelAdmin):
    filter_horizontal = ["members"]
    inlines =[CustomFieldInline]
    


class ComponentAdmin(admin.ModelAdmin):
    pass


class ContractAdmin(admin.ModelAdmin):
    filter_horizontal = ["components"]


class CustomFieldAdmin(admin.ModelAdmin):
    pass


class ReviewCallAdmin(admin.ModelAdmin):
    pass

class TestStatusAdmin(admin.ModelAdmin):
    pass

class SignStatusAdmin(admin.ModelAdmin):
    pass

class LockStatusAdmin(admin.ModelAdmin):
    pass

class ContractTypeAdmin(admin.ModelAdmin):
    pass

class ContractStatusAdmin(admin.ModelAdmin):
    pass

class ComponentTypeAdmin(admin.ModelAdmin):
    pass

class OrganisationRoleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(ReviewCall, ReviewCallAdmin)
admin.site.register(TestStatus, TestStatusAdmin)
admin.site.register(LockStatus, LockStatusAdmin)
admin.site.register(SignStatus, SignStatusAdmin)
admin.site.register(ContractStatus, ContractStatusAdmin)
admin.site.register(ContractType, ContractStatusAdmin)
admin.site.register(OrganisationRole, OrganisationRoleAdmin)
admin.site.register(ComponentType, ComponentTypeAdmin)