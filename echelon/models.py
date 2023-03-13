from django.db import models
from django.template.defaultfilters import slugify

from accounts.models.organisation import Organisation


# Create your models here.
class Level(models.Model):
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


class Class(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Room(models.Model):
    class_fk = models.ManyToManyField(Class, related_name='class_fk')
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Term(models.Model):
    name = models.CharField(max_length=50)
    starts_on = models.DateField()
    ends_on = models.DateField()
    is_active = models.BooleanField(default=True)

    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # created_on = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return self.name
