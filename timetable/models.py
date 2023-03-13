from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from accounts.models.organisation import Organisation
from assessment.models import Exam
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


class TimeSlot(models.Model):
    # class_fk = models.ManyToManyField(Class, blank=True)
    timestamp_from = models.TimeField(blank=True, null=True, default=timezone.now)
    timestamp_to = models.TimeField(blank=True, null=True, default=timezone.now)
    time_from = models.CharField(max_length=20, unique=True, null=False,
                                 blank=False)  # Hour_from:minute_from meridian_from
    time_to = models.CharField(max_length=20, unique=True, null=False, blank=False)  # Hour_to : minute_to  meridian_to
    hour_from = models.IntegerField(null=False, blank=False)
    minute_from = models.IntegerField(null=False, blank=False)
    meridian_from = models.CharField(max_length=3, unique=False, null=False, blank=False)
    hour_to = models.IntegerField(null=False, blank=False)
    minute_to = models.IntegerField(null=False, blank=False)
    meridian_to = models.CharField(max_length=3, unique=False, null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hour_from}:{self.minute_from} {self.meridian_from}" \
               f" - {self.hour_to}:{self.minute_to} {self.meridian_to}"


class Timetable(models.Model):
    class_fk = models.ManyToManyField(Class, blank=True)
    exam = models.ForeignKey(Exam, blank=True, on_delete=models.DO_NOTHING, default=None)
    subject = models.ManyToManyField(Subject, blank=True)
    time_slot = models.ManyToManyField(TimeSlot, blank=True, default=None)
    timetable_type = models.ForeignKey(TimetableType, blank=True, on_delete=models.DO_NOTHING, default=None)
    # day_of_week = models.DateTimeField(blank=True, null=True, default=timezone.now)
    year = models.IntegerField(null=False, blank=False, default=timezone.datetime.now().year)
    is_active = models.BooleanField(default=True)

    # description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.exam.title


class TimetableRecord(models.Model):
    time_slot = models.ForeignKey(TimeSlot, blank=True, on_delete=models.DO_NOTHING)
    event = models.CharField(max_length=150, unique=True, null=False, blank=False)
    day_of_week = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.event

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.event)
        return super().save(*args, **kwargs)
