from django.db import models
from django.template.defaultfilters import slugify

from accounts.models.organisation import Organisation
from accounts.models.user import Student
from echelon.models import Class, Room, Term
from grade.models import GradeMaster
from subject.models import Subject

# Create your models here.
"""
Need to add comments from both the teachers and head teacher or principal.
"""


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


class Exam(models.Model):
    exam_type = models.ForeignKey(ExamType, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    classes = models.ManyToManyField(Class)
    term = models.ForeignKey(Term, on_delete=models.DO_NOTHING)
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


class Result(models.Model):
    PROMOTED = (
        (0, 'No'),
        (1, 'Yes'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=False)
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, blank=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, blank=True)
    total_score = models.IntegerField(null=False, blank=False, default=0)
    average_score = models.IntegerField(null=False, blank=False, default=0)
    promotion = models.SmallIntegerField(choices=PROMOTED, default=0)
    position = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return f"{self.student}"


class Score(models.Model):
    # Should contain a subject
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
    grade = models.ForeignKey(GradeMaster, on_delete=models.CASCADE, blank=True)
    exam_result = models.ForeignKey(Result, on_delete=models.CASCADE, blank=True)
    test_score = models.IntegerField(null=True, blank=True)
    total_mark = models.IntegerField(null=True, blank=True)
    average_mark = models.IntegerField(null=True, blank=True)
    year = models.IntegerField(null=False, blank=False)
    is_processed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=150)

    def __str__(self):
        return self.exam_result.subject.title
