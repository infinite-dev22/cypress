from django.contrib import messages, auth
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from accounts.models.user import UserType, BaseUser


# User Auth Views
def index_base_user(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            base_users = BaseUser.objects.all()

            context = {
                "base_users": base_users
            }
            return render(request, "admin_panel/user/index_base_user.html", context)
        except ObjectDoesNotExist:
            context = {
                "base_users": None
            }
            return render(request, "admin_panel/user/index_base_user.html", context)
    else:
        return redirect('login_admin_user')


def create_user(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method != 'POST':
            user_types = UserType.objects.all()
            context = {
                "user_types": user_types
            }
            return render(request, 'admin_panel/user/create_user.html', context)
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
    else:
        return redirect('login_admin_user')


def edit_user(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method != 'POST':
            user_types = UserType.objects.all()
            user = BaseUser.objects.get(id=pk)
            context = {
                "user": user,
                "user_types": user_types
            }
            return render(request, 'admin_panel/user/create_user.html', context)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            first_name = request.POST['first_name']
            middle_name = request.POST['middle_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            user_type_id = request.POST['user_type']
            user_type = UserType.objects.get(id=user_type_id)  # Error here.
            email = request.POST['email']
            user = BaseUser.objects.get(id=pk)
            user.username = username,
            user.password = password1,
            user.email = email,
            user.first_name = first_name,
            user.middle_name = middle_name,
            user.user_type = user_type,
            user.last_name = last_name
            user.save()
            messages.info(request, "your account details have been updated successfully")
            return redirect('admin_user')
        else:
            messages.info(request, "passwords do not match...")
            return redirect('user_add')
    else:
        return redirect('login_admin_user')


def login(request):
    if request.method != 'POST':
        return render(request, 'admin_panel/auth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    print("Username: " + username + "\nPassword: " + password)

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('admin_dashboard')

    messages.info(request, 'invalid credentials...')
    return redirect('login_admin_user')


def delete_user(request, pk):
    if request.user.is_authenticated:
        BaseUser.objects.get(id=pk).delete()
        return redirect('admin_user')
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
