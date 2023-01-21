from django.db import models
from django.template.defaultfilters import slugify

from accounts.models.organisation import Organisation
from echelon.models import Level, Class
from subject.models import Subject


# Create your models here.
class GradeMaster(models.Model):
    organisation = models.ManyToManyField(Organisation, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)
    review = models.CharField(max_length=150, unique=True, null=False, blank=False)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class GradeDetails(models.Model):
    grade = models.ManyToManyField(GradeMaster, blank=True)
    class_fk = models.ManyToManyField(Class, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    marks_from = models.IntegerField(null=False, blank=False)
    marks_to = models.IntegerField(null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.grade.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.grade.title)
        return super().save(*args, **kwargs)
