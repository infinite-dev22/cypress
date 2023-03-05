from django.contrib import admin

from .models import ExamType, Exam, Result, Score

# Register your models here.
admin.site.register([
    ExamType,
    Exam,
    Result,
    Score,
])
