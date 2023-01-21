from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from accounts.models.organisation import Organisation
from assessment.models import ExamMaster
from echelon.models import Class
from subject.models import Subject


# Create your models here.
class TimetableType(models.Model):
    organisation = models.ManyToManyField(Organisation, blank=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class TimetableRecord(models.Model):
    class_fk = models.ManyToManyField(Class, blank=True)
    exam = models.ManyToManyField(ExamMaster, blank=True)
    timetable_type = models.ManyToManyField(TimetableType, blank=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class TimeSlot(models.Model):
    timetable_record = models.ManyToManyField(TimetableRecord, blank=True)
    timestamp_from = models.DateTimeField(ExamMaster, blank=True, null=True, default=timezone.now)
    timestamp_to = models.DateTimeField(ExamMaster, blank=True, null=True, default=timezone.now)
    # full =
    time_from = models.CharField(max_length=20, unique=True, null=False,
                                 blank=False)  # Hour_from:minute_from meridian_from
    time_to = models.CharField(max_length=20, unique=True, null=False, blank=False)  # Hour_to : minute_to  meridian_to
    hour_from = models.IntegerField(null=False, blank=False)
    minute_from = models.IntegerField(null=False, blank=False)
    meridian_from = models.CharField(max_length=3, unique=True, null=False, blank=False)
    hour_to = models.IntegerField(null=False, blank=False)
    minute_to = models.IntegerField(null=False, blank=False)
    meridian_to = models.CharField(max_length=3, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.timetable_record.title


class Timetable(models.Model):
    subject = models.ManyToManyField(Subject, blank=True)
    timetable_record = models.ManyToManyField(TimetableRecord, blank=True)
    time_slot = models.ManyToManyField(TimeSlot, blank=True)
    day = models.DateTimeField(ExamMaster, blank=True, null=True, default=timezone.now)
    timestamp_from = models.DateTimeField(ExamMaster, blank=True, null=True, default=timezone.now)
    timestamp_to = models.DateTimeField(ExamMaster, blank=True, null=True, default=timezone.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.timetable_record.title
