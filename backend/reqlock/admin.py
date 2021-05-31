from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models.admin_mixins import SoftDeleteAdmin,SoftDeleteInlineAdmin
from .models import *


class CustomFieldInline(SoftDeleteInlineAdmin, GenericStackedInline):
    model = CustomField
    extra = 1


class ProjectAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    filter_horizontal = ["members"]
    inlines = [CustomFieldInline]


class OrganisationAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    filter_horizontal = ["members"]
    inlines = [CustomFieldInline]


class ComponentAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class ContractAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    filter_horizontal = ["components"]
    inlines = [CustomFieldInline]


class CustomFieldAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class ReviewCallAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class TestStatusAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class SignStatusAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class LockStatusAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class ContractTypeAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class ContractStatusAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class ComponentTypeAdmin(SoftDeleteAdmin, admin.ModelAdmin):
    pass


class OrganisationRoleAdmin(SoftDeleteAdmin, admin.ModelAdmin):
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
