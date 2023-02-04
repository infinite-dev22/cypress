from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation
from echelon.models import Level, Class


# Permissions Views
def index_levels(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            levels = Level.objects.all()

            context = {
                "levels": levels
            }
            return render(request, "admin_panel/levels/index_levels.html", context)
        except ObjectDoesNotExist:
            context = {
                "level": None
            }
            return render(request, "admin_panel/levels/index_levels.html", context)
    else:
        return redirect('login_admin_user')


def create_level(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            organisation = request.POST.getlist("organisation")
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            level = Level(
                title=title,
                is_active=is_active,
                description=description
            )
            level.save()
            level.organisation.set(organisation)
            return redirect("admin_level")

        organisations = Organisation.objects.all()
        context = {
            "organisations": organisations
        }
        return render(request, "admin_panel/levels/edit_level.html", context)
    else:
        return redirect('login_admin_user')


def edit_level(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            organisation = request.POST.getlist("organisation")
            description = request.POST["description"]
            is_active = request.POST.get("is_active", False)
            level = Level.objects.get(id=pk)
            level.title = title
            level.organisation = organisation
            level.is_active = is_active
            level.description = description
            level.save()
            return redirect("admin_level")

        level = Level.objects.get(id=pk)
        organisations = Organisation.objects.all()
        context = {
            "level": level,
            "organisations": organisations
        }
        return render(request, "admin_panel/levels/index_level.html", context)
    else:
        return redirect('login_admin_user')


def delete_level(request, pk):
    if request.user.is_authenticated:
        Level.objects.get(id=pk).delete()
        return redirect('admin_level')
    else:
        return redirect('login_admin_user')


# Permissions Views
def index_classes(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            classes = Class.objects.all()

            context = {
                "classes": classes
            }
            return render(request, "admin_panel/classes/index_classes.html", context)
        except ObjectDoesNotExist:
            context = {
                "classes": None
            }
            return render(request, "admin_panel/classes/index_classes.html", context)
    else:
        return redirect('login_admin_user')


def create_class(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            level_id = request.POST["level"]
            title = request.POST["title"]
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            level = Level.objects.get(id=level_id)
            classes = Class(
                level=level,
                title=title,
                is_active=is_active,
                description=description
            )
            classes.save()
            return redirect("admin_class")

        levels = Level.objects.all()
        context = {
            "levels": levels
        }
        return render(request, "admin_panel/classes/edit_class.html", context)
    else:
        return redirect('login_admin_user')


def edit_class(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            level = request.POST["level"]
            title = request.POST["title"]
            description = request.POST["description"]
            is_active = request.POST.get("is_active", False)
            classes = Class.objects.get(id=pk)
            classes.title = title
            classes.level = level
            classes.is_active = is_active
            classes.description = description
            classes.save()
            return redirect("admin_class")

        classes = Class.objects.get(id=pk)
        levels = Level.objects.all()
        context = {
            "levels": levels,
            "classes": classes
        }
        return render(request, "admin_panel/classes/edit_class.html", context)
    else:
        return redirect('login_admin_user')


def delete_class(request, pk):
    if request.user.is_authenticated:
        Class.objects.get(id=pk).delete()
        return redirect('admin_class')
    else:
        return redirect('login_admin_user')
