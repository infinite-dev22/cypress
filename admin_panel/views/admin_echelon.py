from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation
from echelon.models import Level, Class, Room


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
    return redirect('login_admin_user')


def create_level(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            organisation = request.POST.getlist("organisation")
            is_active = request.POST.get("is_active", True)
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
    return redirect('login_admin_user')


def edit_level(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            organisation = request.POST.getlist("organisation")
            description = request.POST["description"]
            is_active = request.POST.get("is_active", True)
            level = Level.objects.get(id=pk)
            level.title = title
            # level.organisation = organisation
            level.is_active = is_active
            level.description = description
            level.save()
            level.organisation.set(organisation)
            return redirect("admin_level")

        level = Level.objects.get(id=pk)
        organisations = Organisation.objects.all()
        context = {
            "level": level,
            "organisations": organisations
        }
        return render(request, "admin_panel/levels/edit_level.html", context)
    return redirect('login_admin_user')


def delete_level(request, pk):
    if request.user.is_authenticated:
        Level.objects.get(id=pk).delete()
        return redirect('admin_level')
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
    return redirect('login_admin_user')


def create_class(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            level_id = request.POST["level"]
            level = Level.objects.get(id=level_id)
            title = request.POST["title"]
            is_active = request.POST.get("is_active", True)
            description = request.POST["description"]
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
    return redirect('login_admin_user')


def edit_class(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            level_id = request.POST["level"]
            level = Level.objects.get(id=level_id)
            title = request.POST["title"]
            description = request.POST["description"]
            is_active = request.POST.get("is_active", True)
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
    return redirect('login_admin_user')


def delete_class(request, pk):
    if request.user.is_authenticated:
        Class.objects.get(id=pk).delete()
        return redirect('admin_class')
    return redirect('login_admin_user')


# Rooms Views
def index_rooms(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            rooms = Room.objects.all()

            context = {
                "rooms": rooms
            }
            return render(request, "admin_panel/rooms/index_rooms.html", context)
        except ObjectDoesNotExist:
            context = {
                "rooms": None
            }
            return render(request, "admin_panel/rooms/index_rooms.html", context)
    return redirect('login_admin_user')


def create_room(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            classes = request.POST["class"]
            title = request.POST["title"]
            is_active = request.POST.get("is_active", True)
            description = request.POST["description"]
            room = Room(
                title=title,
                is_active=is_active,
                description=description
            )
            room.save()
            room.class_fk.set(classes)
            return redirect("admin_room")

        classes = Class.objects.all()
        context = {
            "classes": classes
        }
        return render(request, "admin_panel/rooms/edit_room.html", context)
    return redirect('login_admin_user')


def edit_room(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            classes = request.POST["class"]
            title = request.POST["title"]
            is_active = request.POST.get("is_active", True)
            description = request.POST["description"]
            room = Room.objects.get(id=pk)
            room.title = title
            room.is_active = is_active
            room.description = description
            room.save()
            room.class_fk.set(classes)
            return redirect("admin_room")

        room = Room.objects.get(id=pk)
        classes = Class.objects.all()
        context = {
            "classes": classes,
            "room": room
        }
        return render(request, "admin_panel/rooms/edit_room.html", context)
    return redirect('login_admin_user')


def delete_room(request, pk):
    if request.user.is_authenticated:
        Room.objects.get(id=pk).delete()
        return redirect('admin_room')
    return redirect('login_admin_user')
