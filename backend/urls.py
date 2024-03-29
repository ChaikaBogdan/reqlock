"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from rest_framework import routers
from reqlock import views
from allauth.account.views import confirm_email


router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet, 'project')
router.register(r'organisations', views.OrganisationViewSet, 'organisation')
router.register(r'components', views.ComponentViewSet, 'component')
router.register(r'contracts', views.ContractViewSet, 'contract')

urlpatterns = [
    path(
        'grappelli/',
        include('grappelli.urls')),
    path(
        '',
        admin.site.urls),
    path(
        'api/',
        include(
            router.urls)),
    path(
        'dj-rest-auth/',
        include('dj_rest_auth.urls')),
    # dj_rest_auth/registration/urls.py#L11
    path(
        'dj-rest-auth/registration/account-confirm-email/<str:key>/',
        confirm_email,
        name='account_confirm_email'),
    path(
        'dj-rest-auth/registration/',
        include('dj_rest_auth.registration.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(
        path('debug/', include(debug_toolbar.urls))
    )
