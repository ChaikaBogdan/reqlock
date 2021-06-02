
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.utils.translation import ugettext_lazy as _


class SoftDeleteAdmin(admin.ModelAdmin):
    readonly_fields = ('deleted_at', 'created_at', 'updated_at')

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super().get_fieldsets(request, obj=obj))
        fields_to_remove = ['created_at', 'updated_at', 'deleted_at']
        fields = fieldsets[0][1]['fields']
        fieldsets[0][1]['fields'] = [
            f for f in fields if f not in fields_to_remove]
        if obj and not obj._state.adding:
            fieldsets.append((_('System fields'), {
                'classes': ('grp-collapse grp-closed',),
                'fields': ('created_at', 'updated_at', 'deleted_at',),
            }))
        return fieldsets


class SoftDeleteInlineAdmin(GenericStackedInline):
    def get_fields(self, request, obj=None):
        fields = list(super().get_fields(request, obj=obj))
        fields_to_remove = ['created_at', 'updated_at', 'deleted_at']
        return [f for f in fields if f not in fields_to_remove]


class HiddenModelAdmin():
    def has_module_permission(self, request):
        return False
