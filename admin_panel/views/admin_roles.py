from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from accounts.models.control import Role


# Permissions Views
def index_roles(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            roles = Role.objects.all()
            print(roles)

            context = {
                "roles": roles
            }
            return render(request, "admin_panel/roles/index_roles.html", context)
        except ObjectDoesNotExist:
            context = {
                "roles": None
            }
            return render(request, "admin_panel/roles/index_roles.html", context)
    else:
        return redirect('login_admin_user')


def create_role(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            permission = request.POST.getlist("permission")
            is_active = request.POST.get("is_active", True)
            description = request.POST["description"]
            role = Role(
                title=title,
                is_active=is_active,
                description=description
            )
            role.save()
            role.permission.set(permission)
            return redirect("admin_role")

        permissions = Permission.objects.all()
        context = {
            "permissions": permissions
        }
        return render(request, "admin_panel/roles/edit_role.html", context)
    else:
        return redirect('login_admin_user')


def edit_role(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            permission = request.POST.getlist("permission")
            description = request.POST["description"]
            is_active = request.POST.get("is_active", True)
            role = Role.objects.get(id=pk)
            role.title = title
            # role.permission = permission
            role.is_active = is_active
            role.description = description
            role.save()
            role.permission.set(permission)
            return redirect("admin_role")

        role = Role.objects.get(id=pk)
        permissions = Permission.objects.all()
        context = {
            "role": role,
            "permissions": permissions
        }
        return render(request, "admin_panel/roles/edit_role.html", context)
    else:
        return redirect('login_admin_user')


def delete_roles(request, pk):
    if request.user.is_authenticated:
        Role.objects.get(id=pk).delete()
        return redirect('admin_role')
    else:
        return redirect('login_admin_user')
