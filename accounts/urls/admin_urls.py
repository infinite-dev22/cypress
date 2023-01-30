"""cypress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from accounts.views import admin_views

DASHBOARD_URLS = [
    path('dash', admin_views.dashboard_admin, name="admin_dashboard"),
]

ORGANISATION_URLS = [
    path('organisation/', admin_views.index_organisation, name="admin_org"),
    path('organisation/profiles', admin_views.index_organisation_profile, name="admin_org_profiles"),
    path('organisation/add/', admin_views.create_organisation, name="org_add"),
    path('organisation/add/<int:pk>', admin_views.edit_organisation, name="org_edit"),

]

CONTROLS_URLS = [
    path('role/', admin_views.index_roles, name="admin_role"),
    path('role/add/', admin_views.create_role, name="role_add"),
    path('role/add/<int:pk>', admin_views.edit_role, name="role_edit"),
]

USER_URLS = [
    # UserType Urls
    path('user_type/', admin_views.index_user_type, name="admin_user_type"),
    path('user_type/add/', admin_views.create_user_type, name="user_type_add"),
    path('user_type/add/<int:pk>', admin_views.edit_user_type, name="user_type_edit"),

    # User Urls
    path('user/', admin_views.index_base_user, name="admin_user"),
    path('user/add/', admin_views.create_user, name="user_add"),
    path('login/', admin_views.login, name="login_admin_user"),
    path('', admin_views.logout, name="admin_user_logout"),

]

urlpatterns = DASHBOARD_URLS + ORGANISATION_URLS + CONTROLS_URLS + USER_URLS
