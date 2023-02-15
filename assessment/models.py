from django.db import models
from django.template.defaultfilters import slugify

from accounts.models.organisation import Organisation
from echelon.models import Class, Room
from grade.models import GradeMaster
from subject.models import Subject


# Create your models here.
class ExamType(models.Model):
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
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


class ExamMaster(models.Model):
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    classes = models.ManyToManyField(Class)
    term = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class ExamResult(models.Model):
    exam_master = models.ManyToManyField(ExamMaster, blank=True)
    class_fk = models.ManyToManyField(Class, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    room = models.ManyToManyField(Room, blank=True)
    position = models.IntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.subject.title


class Marks(models.Model):
    grade = models.ManyToManyField(GradeMaster, blank=True)
    exam_result = models.ManyToManyField(ExamResult, blank=True)
    test_1 = models.IntegerField(null=False, blank=False)
    test_2 = models.IntegerField(null=False, blank=False)
    test_3 = models.IntegerField(null=False, blank=False)
    test_4 = models.IntegerField(null=False, blank=False)
    total_mark = models.IntegerField(null=False, blank=False)
    average_mark = models.IntegerField(null=False, blank=False)
    year = models.IntegerField(null=False, blank=False)
    is_processed = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.exam_result.subject.title
