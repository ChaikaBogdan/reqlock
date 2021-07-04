from django.contrib.admin.apps import AdminConfig


class ReqlockAdminConfig(AdminConfig):
    default_site = 'admin.ReqlockAdminSite'
