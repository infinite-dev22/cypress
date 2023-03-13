from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from accounts.models.control import Role
from accounts.models.user import UserType


# User Views
def index_user_type(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            user_types = UserType.objects.all()

            context = {
                "user_types": user_types
            }
            return render(request, "admin_panel/user/index_user_type.html", context)
        except ObjectDoesNotExist:
            context = {
                "user_types": None
            }
            return render(request, "admin_panel/user/index_user_type.html", context)
    else:
        return redirect('login_admin_user')


def create_user_type(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            role = request.POST.getlist("role")
            is_active = request.POST.get("is_active", True)
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
        return render(request, "admin_panel/user/edit_user_type.html", context)
    else:
        return redirect('login_admin_user')


def edit_user_type(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            role = request.POST.getlist("role")
            is_active = request.POST.get("is_active", True)
            description = request.POST["description"]
            user_type = UserType.objects.get(id=pk)
            user_type.title = title
            user_type.is_active = is_active
            user_type.description = description
            user_type.save()
            user_type.role.set(role)
            return redirect("admin_user_type")

        user_type = UserType.objects.get(id=pk)
        roles = Role.objects.all()
        context = {
            "user_type": user_type,
            "roles": roles
        }
        return render(request, "admin_panel/user/edit_user_type.html", context)
    else:
        return redirect('login_admin_user')


def delete_user_type(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        UserType.objects.get(id=pk).delete()
        return redirect("admin_user_type")
    return redirect('login_admin_user')
