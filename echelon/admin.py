from django.contrib import admin

from .models import Level, Class, Room

# Register your models here.
admin.site.register([
    Level,
    Class,
    Room,
])
