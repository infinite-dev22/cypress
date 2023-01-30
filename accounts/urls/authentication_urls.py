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
from accounts.views import authentication_views

USER_URLS = [
    # UserType Urls
    path('user_type/', admin_views.index_user_type, name="admin_user_type"),
    path('user_type/add/', admin_views.create_user_type, name="user_type_add"),
    path('user_type/add/<int:pk>', admin_views.edit_user_type, name="user_type_edit"),

    # User Urls
    path('register/', authentication_views.register_organisation, name="register"),
    path('register/user/<org>', authentication_views.create_head_teacher, name="register_super_admin"),
    path('login/', authentication_views.login, name="login_user"),
    path('', authentication_views.logout, name="user_logout"),
    path('user/', authentication_views.index_base_user, name="users"),
    path('user/add/', authentication_views.create_user, name="user_add"),

]

urlpatterns = USER_URLS
