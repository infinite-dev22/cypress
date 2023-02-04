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

from admin_panel.views import admin_users, organisation_views, admin_roles, admin_user_types, admin_dashboard, \
    admin_echelon, admin_students

DASHBOARD_URLS = [
    path('', admin_dashboard.dashboard_admin, name="admin_dashboard"),
]

ORGANISATION_URLS = [
    path('organisation/', organisation_views.index_organisation, name="admin_org"),
    path('organisation/profiles', organisation_views.index_organisation_profile, name="admin_org_profiles"),
    path('organisation/add/', organisation_views.create_organisation, name="org_add"),
    path('organisation/add/<int:pk>', organisation_views.edit_organisation, name="org_edit"),
    path('organisation/del/<int:pk>', organisation_views.delete_org, name="org_del"),
]

CONTROLS_URLS = [
    path('role/', admin_roles.index_roles, name="admin_role"),
    path('role/add/', admin_roles.create_role, name="role_add"),
    path('role/add/<int:pk>', admin_roles.edit_role, name="role_edit"),
    path('role/del/<int:pk>', admin_roles.delete_roles, name="role_del"),
]

USER_URLS = [
    # UserType Urls
    path('user_type/', admin_user_types.index_user_type, name="admin_user_type"),
    path('user_type/add/', admin_user_types.create_user_type, name="user_type_add"),
    path('user_type/add/<int:pk>', admin_user_types.edit_user_type, name="user_type_edit"),

    # User Urls
    path('user/', admin_users.index_base_user, name="admin_user"),
    path('user/add/', admin_users.create_user, name="user_add"),
    path('login/', admin_users.login, name="login_admin_user"),
    path('logout/', admin_users.logout, name="admin_user_logout"),
]

LEVELS_URLS = [
    path('level/', admin_echelon.index_levels, name="admin_level"),
    path('level/add/', admin_echelon.create_level, name="level_add"),
    path('level/add/<int:pk>', admin_echelon.edit_level, name="level_edit"),
    path('level/del/<int:pk>', admin_echelon.delete_level, name="level_del"),
]

CLASSES_URLS = [
    path('class/', admin_echelon.index_classes, name="admin_class"),
    path('class/add/', admin_echelon.create_class, name="class_add"),
    path('class/add/<int:pk>', admin_echelon.edit_class, name="class_edit"),
    path('class/del/<int:pk>', admin_echelon.delete_class, name="class_del"),
]

STUDENTS_URLS = [
    path('students/', admin_students.index_students, name="admin_student"),
    path('student/add/', admin_students.create_student, name="student_add"),
    path('student/add/<int:pk>', admin_students.edit_student, name="student_edit"),
    path('student/del/<int:pk>', admin_students.delete_student, name="student_del"),
]

urlpatterns = DASHBOARD_URLS \
              + ORGANISATION_URLS \
              + CONTROLS_URLS \
              + USER_URLS \
              + LEVELS_URLS \
              + CLASSES_URLS \
              + STUDENTS_URLS
