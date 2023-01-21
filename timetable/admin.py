from django.contrib import admin

from .models import TimetableType, TimetableRecord, TimeSlot, Timetable

# Register your models here.
admin.site.register([
    TimetableType,
    TimetableRecord,
    TimeSlot,
    Timetable,
])
