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

from echelon import views

LEVELS_URLS = [
    path('level/', views.index_levels, name="levels"),
    path('level/add/', views.create_level, name="level_add"),
    path('level/add/<int:pk>', views.edit_level, name="level_edit"),
    path('level/del/<int:pk>', views.delete_level, name="level_del"),
]

TERMS_URLS = [
    path('terms/', views.index_terms, name="terms"),
    path('term/add/', views.create_term, name="term_add"),
    path('term/add/<int:pk>', views.edit_term, name="term_edit"),
    path('term/del/<int:pk>', views.delete_term, name="term_del"),
]

CLASSES_URLS = [
    path('class/', views.index_classes, name="classes"),
    path('class/add/', views.create_class, name="class_add"),
    path('class/add/<int:pk>', views.edit_class, name="class_edit"),
    path('class/del/<int:pk>', views.delete_class, name="class_del"),
]

ROOMS_URLS = [
    path('room/', views.index_rooms, name="rooms"),
    path('room/add/', views.create_room, name="room_add"),
    path('room/add/<int:pk>', views.edit_room, name="room_edit"),
    path('room/del/<int:pk>', views.delete_room, name="room_del"),
]

urlpatterns = LEVELS_URLS \
              + TERMS_URLS \
              + CLASSES_URLS \
              + ROOMS_URLS
