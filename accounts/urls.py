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

from accounts import views
from admin_panel.views import admin_user_types

USER_URLS = [
    # UserType Urls
    path('user_type/', admin_user_types.index_user_type, name="user_type"),
    path('user_type/add/', admin_user_types.create_user_type, name="user_type_add"),
    path('user_type/add/<int:pk>', admin_user_types.edit_user_type, name="user_type_edit"),

    # User Urls
    path('register/', views.register_organisation, name="register"),
    path('register/user/<org>', views.create_head_teacher, name="register_super_admin"),
    path('login/', views.login, name="login_user"),
    path('', views.logout, name="user_logout"),
    path('user/', views.index_user, name="users"),
    path('user/add/', views.create_user, name="user_add"),
    path('user/remove/<pk>', views.delete_user, name="delete_users"),
]

urlpatterns = USER_URLS
