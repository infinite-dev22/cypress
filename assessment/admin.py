from django.contrib import admin

from .models import ExamType, ExamMaster, ExamResult, Marks

# Register your models here.
admin.site.register([
    ExamType,
    ExamMaster,
    ExamResult,
    Marks,
])
