from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from accounts.models.organisation import Organisation, OrganisationProfile
from accounts.models.user import UserType, BaseUser


def register_organisation(request):
    if request.method != 'POST':
        return render(request, 'accounts/authentication/user/register.html')
    if request.method == "POST":
        title = request.POST["title"]
        org = Organisation(
            title=title,
            is_active=True,
        )
        org.save()
        org_profile = OrganisationProfile(organisation=org, is_active=True)
        org_profile.save()
        context = {
            "org": org
        }
        return redirect("register_super_admin", org=org)


def create_head_teacher(request, org):
    if request.method != 'POST':
        context = {
            "org": org
        }
        print("Over Here")
        return render(request, 'accounts/authentication/user/create_main_user.html', context)

    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
        organisation = request.POST['org_id']
        username = request.POST['username']
        user_type = UserType.objects.get(title="HeadTeacher")
        email = request.POST['email']
        if BaseUser.objects.filter(username=username).exists():
            messages.info(request, "username taken...")
            return redirect('register_super_admin', org=org)

        if BaseUser.objects.filter(email=email).exists():
            messages.info(request, "email taken...")
            return redirect('register_super_admin', org=org)

        user = BaseUser.objects.create_user(
            username=username,
            password=password1,
            email=email,
            user_type=user_type,
        )
        user.save()
        user.organisation.set(organisation)

        messages.info(request, "your account has been created successfully")
        return redirect('dashboard')

    messages.info(request, "passwords do not match...")
    return redirect('register_super_admin', org=org)


# User Auth Views
def index_base_user(request):
    try:
        base_users = BaseUser.objects.all()

        context = {
            "base_users": base_users
        }
        return render(request, "accounts/authentication/user/index_base_user.html", context)
    except ObjectDoesNotExist:
        context = {
            "base_users": None
        }
        return render(request, "accounts/authentication/user/index_base_user.html", context)


def create_user(request):
    if request.method != 'POST':
        user_types = UserType.objects.all()
        context = {
            "user_types": user_types
        }
        return render(request, 'accounts/authentication/user/create_user.html', context)
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

        if BaseUser.objects.filter(email=email).exists():
            messages.info(request, "email taken...")
            return redirect('admin_user')

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

    messages.info(request, "passwords do not match...")
    return redirect('user_add')


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/authentication/user/login.html')

    identifier = request.POST['identifier']
    password = request.POST['password']

    print("Username: " + identifier + "\nPassword: " + password)

    user = auth.authenticate(username=identifier, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('dashboard')

    messages.info(request, 'invalid credentials...')
    return redirect('login')


def logout(request):
    auth.logout(request)
    return redirect('login_user')


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
