from django.contrib import admin

from .models.control import Permissions, Role
from .models.organisation import OrganisationType, Organisation, OrganisationProfile
from .models.user import BaseUser, UserType, HeadTeacher, Teacher, NormalUser

# Register your models here.
admin.site.register([
    # user
    UserType,
    BaseUser,
    HeadTeacher,
    Teacher,
    NormalUser,

    # Control
    Permissions,
    Role,

    # organisation
    OrganisationType,
    Organisation,
    OrganisationProfile,
])
