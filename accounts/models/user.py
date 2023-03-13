from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.template.defaultfilters import slugify

from echelon.models import Class
from subject.models import Subject
from .control import Role
from .manager import CustomUserManager
from .organisation import Organisation


class UserType(models.Model):
    title = models.CharField(max_length=150, unique=True, null=False, blank=False)
    role = models.ManyToManyField(Role, blank=True)
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


class BaseUser(AbstractBaseUser, PermissionsMixin):
    organisation = models.ForeignKey(Organisation, blank=False, on_delete=models.DO_NOTHING)
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, null=True)
    first_name = models.CharField(max_length=150, unique=False, null=False, blank=False)
    middle_name = models.CharField(max_length=150, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=150, unique=False, null=False, blank=False)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.CharField(max_length=150, unique=True, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    slug = models.SlugField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    # custom save function, creates slug from title on save
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        return super().save(*args, **kwargs)


class User(BaseUser):
    """
        Parents, Librarians, Accountants/Bursars, Headteachers
    """
    telephone_1 = models.CharField(max_length=15, unique=False, null=False, blank=False)
    telephone_2 = models.CharField(max_length=15, unique=False, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='headteachers_photos/', null=True)


class Teacher(BaseUser):
    telephone_1 = models.CharField(max_length=15, unique=True, null=False, blank=False)
    telephone_2 = models.CharField(max_length=15, unique=True, null=True, blank=True)
    school_class = models.ManyToManyField(Class, blank=False)
    subject = models.ManyToManyField(Subject, blank=False)
    profile_pic = models.ImageField(upload_to='teachers_photos/', null=True)


class Student(BaseUser):
    parents = models.ManyToManyField(User, blank=True)
    class_fk = models.ForeignKey(Class, related_name='student', on_delete=models.CASCADE, null=True)
    subject = models.ManyToManyField(Subject, blank=False)  # Attach all non-option subjects
    profile_pic = models.ImageField(upload_to='students_photos/', null=True)
