from django.contrib import admin

from .models import GradeMaster, GradeDetails

# Register your models here.
admin.site.register([
    GradeMaster,
    GradeDetails,
])
