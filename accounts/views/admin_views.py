from django.contrib import messages, auth
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from accounts.models.control import Role
from accounts.models.organisation import Organisation, OrganisationProfile
from accounts.models.user import UserType, BaseUser


# Dashboard Views
@user_passes_test(lambda u: u.is_superuser, login_url='login_admin_user')
def dashboard_admin(request):
    return render(request, "accounts/admin/dashboard.html")


# Organisation Views
def index_organisation(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            orgs = Organisation.objects.all()
            context = {
                "orgs": orgs
            }
            return render(request, "accounts/admin/index_org.html", context)
        except ObjectDoesNotExist:
            context = {
                "orgs": None
            }
            return render(request, "accounts/admin/index_org.html", context)
    else:
        return redirect('login_admin_user')


def create_organisation(request):
    if request.method == "POST":
        title = request.POST["title"]
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        org = Organisation(
            title=title,
            is_active=is_active,
            description=description
        )
        org.save()
        org_profile = OrganisationProfile(organisation=org, is_active=is_active)
        org_profile.save()
        return redirect("admin_org")

    return render(request, "accounts/admin/edit_org.html")


def edit_organisation(request, pk):
    if request.method == "POST":
        organisation = request.POST["organisation"]
        telephone_1 = request.POST["telephone_1"]
        telephone_2 = request.POST["telephone_2"]
        fax = request.POST["fax"]
        email = request.POST["email"]
        website = request.POST["website"]
        post_address = request.POST["post_address"]
        physical_address = request.POST["physical_address"]
        logo = request.POST["logo"]
        title = request.POST["title"]
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        org = Organisation.objects.get(id=pk)
        org.title = title
        org.is_active = is_active
        org.description = description
        org.save()
        org_profile = OrganisationProfile.objects.all().filter(organisation=org)
        org_profile.organisation = organisation
        org_profile.telephone_1 = telephone_1
        org_profile.telephone_2 = telephone_2
        org_profile.fax = fax
        org_profile.email = email
        org_profile.website = website
        org_profile.post_address = post_address
        org_profile.physical_address = physical_address
        org_profile.logo = logo
        org_profile.is_active = is_active
        org_profile.save()
        return redirect("admin_org")

    org = Organisation.objects.get(id=pk)
    org_profile = OrganisationProfile.objects.all().filter(organisation=org)
    context = {
        "org": org,
        "profile": org_profile
    }
    return render(request, "accounts/admin/edit_org.html", context)


# Organisation Profile Views
def index_organisation_profile(request):
    try:
        org_profiles = OrganisationProfile.objects.all()
        context = {
            "org_profiles": org_profiles
        }
        return render(request, "accounts/admin/index_org_profiles.html", context)
    except ObjectDoesNotExist:
        context = {
            "org_profiles": None
        }
        return render(request, "accounts/admin/index_org_profiles.html", context)


def edit_organisation_profile(request, pk=None):
    if request.method == "POST":
        organisation = request.POST["organisation"]
        telephone_1 = request.POST["telephone_1"]
        telephone_2 = request.POST["telephone_2"]
        fax = request.POST["fax"]
        email = request.POST["email"]
        website = request.POST["website"]
        post_address = request.POST["post_address"]
        physical_address = request.POST["physical_address"]
        logo = request.POST["logo"]
        is_active = request.POST.get("is_active", False)
        OrganisationProfile(
            organisation=organisation,
            telephone_1=telephone_1,
            telephone_2=telephone_2,
            fax=fax,
            email=email,
            website=website,
            post_address=post_address,
            physical_address=physical_address,
            logo=logo,
            is_active=is_active
        ).save()
        return redirect("admin_org")

    if pk is not None and request.method == "POST":
        organisation = request.POST["organisation"]
        telephone_1 = request.POST["telephone_1"]
        telephone_2 = request.POST["telephone_2"]
        fax = request.POST["fax"]
        email = request.POST["email"]
        website = request.POST["website"]
        post_address = request.POST["post_address"]
        physical_address = request.POST["physical_address"]
        logo = request.POST["logo"]
        is_active = request.POST.get("is_active", False)
        org_profile = OrganisationProfile.objects.get(id=pk)
        org_profile.organisation = organisation
        org_profile.telephone_1 = telephone_1
        org_profile.telephone_2 = telephone_2
        org_profile.fax = fax
        org_profile.email = email
        org_profile.website = website
        org_profile.post_address = post_address
        org_profile.physical_address = physical_address
        org_profile.logo = logo
        org_profile.is_active = is_active
        org_profile.save()
        return redirect("admin_org")

    return render(request, "accounts/admin/edit_profile.html")


# Permissions Views
def index_roles(request):
    try:
        roles = Role.objects.all()
        print(roles)

        context = {
            "roles": roles
        }
        return render(request, "accounts/admin/control/index_roles.html", context)
    except ObjectDoesNotExist:
        context = {
            "roles": None
        }
        return render(request, "accounts/admin/control/index_roles.html", context)


def create_role(request):
    if request.method == "POST":
        title = request.POST["title"]
        permission = request.POST.getlist("permission")
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        role = Role(
            title=title,
            is_active=is_active,
            description=description
        )
        role.save()
        for p in permission:
            print(p)
        role.permission.set(permission)
        return redirect("admin_role")

    permissions = Permission.objects.all()
    context = {
        "permissions": permissions
    }
    return render(request, "accounts/admin/control/edit_role.html", context)


def edit_role(request, pk):
    if request.method == "POST":
        title = request.POST["title"]
        permission = request.POST.getlist("permission")
        description = request.POST["description"]
        is_active = request.POST.get("is_active", False)
        role = Role.objects.get(id=pk)
        role.title = title
        role.permission = permission
        role.is_active = is_active
        role.description = description
        role.save()
        return redirect("admin_role")

    role = Role.objects.get(id=pk)
    permissions = Permission.objects.all()
    context = {
        "role": role,
        "permission": permissions
    }
    return render(request, "accounts/admin/control/edit_role.html", context)


# User Views
def index_user_type(request):
    try:
        user_types = UserType.objects.all()

        context = {
            "user_types": user_types
        }
        return render(request, "accounts/admin/user/index_user_type.html", context)
    except ObjectDoesNotExist:
        context = {
            "user_types": None
        }
        return render(request, "accounts/admin/user/index_user_type.html", context)


def create_user_type(request):
    if request.method == "POST":
        title = request.POST["title"]
        role = request.POST.getlist("role")
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        user_type = UserType(
            title=title,
            is_active=is_active,
            description=description
        )
        user_type.save()
        user_type.role.set(role)
        return redirect("admin_user_type")

    roles = Role.objects.all()
    context = {
        "roles": roles
    }
    return render(request, "accounts/admin/user/edit_user_type.html", context)


def edit_user_type(request, pk):
    if request.method == "POST":
        title = request.POST["title"]
        role = request.POST.getlist("role")
        is_active = request.POST.get("is_active", False)
        description = request.POST["description"]
        user_type = UserType.objects.get(id=pk)
        user_type.title = title
        user_type.is_active = is_active
        user_type.description = description
        user_type.save()
        user_type.permission.set(role)
        return redirect("admin_user_type")

    user_type = UserType.objects.get(id=pk)
    roles = Role.objects.all()
    context = {
        "user_type": user_type,
        "roles": roles
    }
    return render(request, "accounts/admin/control/edit_role.html", context)


# User Auth Views
def index_base_user(request):
    try:
        base_users = BaseUser.objects.all()

        context = {
            "base_users": base_users
        }
        return render(request, "accounts/admin/user/index_base_user.html", context)
    except ObjectDoesNotExist:
        context = {
            "base_users": None
        }
        return render(request, "accounts/admin/user/index_base_user.html", context)


def create_user(request):
    if request.method != 'POST':
        user_types = UserType.objects.all()
        context = {
            "user_types": user_types
        }
        return render(request, 'accounts/admin/user/create_user.html', context)
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        user_type_id = request.POST['user_type']
        user_type = UserType.objects.get(id=user_type_id)
        email = request.POST['email']
        if BaseUser.objects.filter(username=username).exists():
            messages.info(request, "username taken...")
            return redirect('register')
        elif BaseUser.objects.filter(email=email).exists():
            messages.info(request, "email taken...")
            return redirect('admin_user')
        else:
            user = BaseUser.objects.create_user(
                username=username,
                password=password1,
                email=email,
                first_name=first_name,
                middle_name=middle_name,
                user_type=user_type,
                last_name=last_name
            )
            user.save()
            messages.info(request, "your account has been created successfully")
            return redirect('admin_user')
    else:
        messages.info(request, "passwords do not match...")
        return redirect('user_add')


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/admin/auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    print("Username: " + username + "\nPassword: " + password)

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('admin_dashboard')

    messages.info(request, 'invalid credentials...')
    return redirect('login_admin_user')


def logout(request):
    auth.logout(request)
    return redirect('login_admin_user')


def get_image_html(url):
    return format_html(
        '<a target="_blank" href="{0}">'
        '<div style="background-image: url(\'{0}\'); '
        'background-position: center; height: 100px; width: 100px; background-size: cover"></div>'
        '</a>'.format(url))


def format_picture(item):
    if item.profile_pic:
        thumbnail = get_thumbnail(item.profile_pic, '200x200', crop='center', quality=99)
        return get_image_html(thumbnail.url)
