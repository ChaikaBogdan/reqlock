from django.contrib import admin
from .models.admin_mixins import SoftDeleteAdmin,SoftDeleteInlineAdmin, HiddenModelMixin
from .models import *


class CustomFieldInline(SoftDeleteInlineAdmin):
    model = CustomField
    extra = 1


class ProjectAdmin(SoftDeleteAdmin):
    filter_horizontal = ["members"]
    inlines = [CustomFieldInline]


class OrganisationAdmin(SoftDeleteAdmin):
    filter_horizontal = ["members"]
    inlines = [CustomFieldInline]


class ComponentAdmin(SoftDeleteAdmin):
    pass


class ContractAdmin(SoftDeleteAdmin):
    filter_horizontal = ["components"]
    inlines = [CustomFieldInline]


class CustomFieldAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class ReviewCallAdmin(SoftDeleteAdmin):
    pass


class TestStatusAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class SignStatusAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class LockStatusAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class ContractTypeAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class ContractStatusAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class ComponentTypeAdmin(HiddenModelMixin, SoftDeleteAdmin):
    pass


class OrganisationRoleAdmin(HiddenModelMixin, SoftDeleteAdmin):
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
