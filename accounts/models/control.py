from django.contrib.auth.models import Permission
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Role(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    permission = models.ManyToManyField(Permission, blank=True)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
