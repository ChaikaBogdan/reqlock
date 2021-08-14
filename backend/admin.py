from django.contrib import admin


class ReqlockAdminSite(admin.AdminSite):
    # https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.AdminSite.final_catch_all_view
    # Default True value breaking rest api routing
    final_catch_all_view = False
