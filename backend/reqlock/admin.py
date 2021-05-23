from django.contrib import admin

from .models import *


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ["members"]


class OrganisationAdmin(admin.ModelAdmin):
    filter_horizontal = ["members"]


class ComponentAdmin(admin.ModelAdmin):
    pass


class ContractAdmin(admin.ModelAdmin):
    filter_horizontal = ["components"]


class CustomFieldAdmin(admin.ModelAdmin):
    pass


class ReviewCallAdmin(admin.ModelAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Organisation, OrganisationAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(ReviewCall, ReviewCallAdmin)
