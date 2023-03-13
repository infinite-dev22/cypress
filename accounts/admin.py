from django.contrib import admin

from .models.control import Role
from .models.organisation import Organisation, OrganisationProfile
from .models.user import BaseUser, UserType, Student, Teacher

# Register your models here.
admin.site.register([
    # user
    UserType,
    BaseUser,
    Student,
    Teacher,

    # Control
    Role,

    # organisation
    Organisation,
    OrganisationProfile,
])
