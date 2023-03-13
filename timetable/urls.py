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

from . import views

TYPES_URLS = [
    path('timetables/types/', views.index_timetable_type, name="timetable_types"),
    path('timetables/types/create/', views.create_timetable_type, name="timetable_type_add"),
    path('timetables/types/<int:pk>', views.edit_timetable_type, name="timetable_type_edit"),
    path('timetables/types/del/<int:pk>', views.delete_timetable_type, name="timetable_type_del"),
]

RECORDS_URLS = [
    path('timetables/records/', views.index_timetable_record, name="timetable_records"),
    path('timetables/records/create/', views.create_timetable_record, name="timetable_record_add"),
    path('timetables/records/<int:pk>', views.edit_timetable_record, name="timetable_record_edit"),
    path('timetables/records/del/<int:pk>', views.delete_timetable_record, name="timetable_record_del"),
]

TIME_SLOTS_URLS = [
    path('timetables/slots/', views.index_time_slot, name="time_slots"),
    path('timetables/slots/create/', views.create_time_slot, name="time_slot_add"),
    path('timetables/slots/<int:pk>', views.edit_time_slot, name="time_slot_edit"),
    path('timetables/slots/del/<int:pk>', views.delete_time_slot, name="time_slot_del"),
]

TIMETABLES_URLS = [
    path('timetables/', views.index_timetable, name="timetables"),
    path('timetables/create/', views.create_timetable, name="timetable_add"),
    path('timetables/<int:pk>', views.edit_timetable, name="timetable_edit"),
    path('timetables/del/<int:pk>', views.delete_timetable, name="timetable_del"),
]

urlpatterns = TYPES_URLS \
              + RECORDS_URLS \
              + TIME_SLOTS_URLS \
              + TIMETABLES_URLS
