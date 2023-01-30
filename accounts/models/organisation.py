from django.db import models
from django.template.defaultfilters import slugify


class Organisation(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
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


class OrganisationProfile(models.Model):
    post_address = models.TextField(null=True, blank=True)
    physical_address = models.TextField(null=True, blank=True)
    email = models.CharField(max_length=150, unique=False, null=True, blank=True)
    website = models.CharField(max_length=150, unique=False, null=True, blank=True)
    telephone_1 = models.CharField(max_length=15, unique=False, null=False, blank=False)
    telephone_2 = models.CharField(max_length=15, unique=False, null=True, blank=True)
    fax = models.CharField(max_length=150, unique=False, null=True, blank=True)
    organisation = models.OneToOneField(Organisation, on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField(max_length=150)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='orgs_logos/', null=True)

    def __str__(self):
        return f"{self.organisation.title}"

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.organisation.title)
        return super().save(*args, **kwargs)
