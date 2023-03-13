from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation
from echelon.models import Level, Class, Room, Term


# Echelon Views
@login_required(login_url='login_user')
def index_terms(request):
    try:
        terms = Term.objects.all()

        context = {
            "terms": terms
        }
        return render(request, "echelon/index_terms.html", context)
    except ObjectDoesNotExist:
        context = {
            "terms": None
        }
        return render(request, "echelon/index_terms.html", context)


@login_required(login_url='login_user')
def create_term(request):
    if request.method == "POST":
        name = request.POST["name"]
        starts_on = request.POST["starts_on"]
        ends_on = request.POST["ends_on"]
        is_active = request.POST.get("is_active", True)
        term = Term(
            name=name,
            starts_on=starts_on,
            ends_on=ends_on,
            is_active=is_active,
        )
        term.save()
        return redirect("terms")
    return render(request, "echelon/edit_term.html")


@login_required(login_url='login_user')
def edit_term(request, pk):
    if request.method == "POST":
        name = request.POST["name"]
        starts_on = request.POST["starts_on"]
        ends_on = request.POST["ends_on"]
        is_active = request.POST.get("is_active", True)
        term = Term.objects.get(id=pk)
        term.name = name
        term.starts_on = starts_on
        term.ends_on = ends_on
        term.is_active = is_active
        term.save()
        return redirect("terms")

    term = Term.objects.get(id=pk)
    context = {
        "term": term,
    }
    print(term)
    return render(request, "echelon/edit_term.html", context)


@login_required(login_url='login_user')
def delete_term(request, pk):
    Term.objects.get(id=pk).delete()
    return redirect('terms')


@login_required(login_url='login_user')
def index_levels(request):
    try:
        levels = Level.objects.all()

        context = {
            "levels": levels
        }
        return render(request, "echelon/index_levels.html", context)
    except ObjectDoesNotExist:
        context = {
            "level": None
        }
        return render(request, "echelon/index_levels.html", context)


@login_required(login_url='login_user')
def create_level(request):
    if request.method == "POST":
        title = request.POST["title"]
        organisation = request.POST.getlist("organisation")
        is_active = request.POST.get("is_active", True)
        description = request.POST["description"]
        level = Level(
            organisation=request.user.organisation,
            title=title,
            is_active=is_active,
            description=description
        )
        level.save()
        level.organisation.set(organisation)
        return redirect("levels")

    organisations = Organisation.objects.all()
    context = {
        "organisations": organisations
    }
    return render(request, "echelon/edit_level.html", context)


@login_required(login_url='login_user')
def edit_level(request, pk):
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
        return redirect("levels")

    level = Level.objects.get(id=pk)
    organisations = Organisation.objects.all()
    context = {
        "level": level,
        "organisations": organisations
    }
    return render(request, "echelon/edit_level.html", context)


@login_required(login_url='login_user')
def delete_level(request, pk):
    Level.objects.get(id=pk).delete()
    return redirect('levels')


# Permissions Views
@login_required(login_url='login_user')
def index_classes(request):
    try:
        classes = Class.objects.all()

        context = {
            "classes": classes
        }
        return render(request, "echelon/index_classes.html", context)
    except ObjectDoesNotExist:
        context = {
            "classes": None
        }
        return render(request, "echelon/index_classes.html", context)


@login_required(login_url='login_user')
def create_class(request):
    if request.method == "POST":
        level_id = request.POST["level"]
        level = Level.objects.get(id=level_id)
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        classes = Class(
            level=level,
            title=title,
            is_active=is_active
        )
        classes.save()
        return redirect("classes")

    levels = Level.objects.all()
    context = {
        "levels": levels
    }
    return render(request, "echelon/edit_class.html", context)


@login_required(login_url='login_user')
def edit_class(request, pk):
    if request.method == "POST":
        level_id = request.POST["level"]
        level = Level.objects.get(id=level_id)
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        classes = Class.objects.get(id=pk)
        classes.title = title
        classes.level = level
        classes.is_active = is_active
        classes.save()
        return redirect("classes")

    classes = Class.objects.get(id=pk)
    levels = Level.objects.all()
    context = {
        "levels": levels,
        "classes": classes
    }
    return render(request, "echelon/edit_class.html", context)


@login_required(login_url='login_user')
def delete_class(request, pk):
    Class.objects.get(id=pk).delete()
    return redirect('classes')


# Rooms Views
@login_required(login_url='login_user')
def index_rooms(request):
    try:
        rooms = Room.objects.all()

        context = {
            "rooms": rooms
        }
        return render(request, "echelon/index_rooms.html", context)
    except ObjectDoesNotExist:
        context = {
            "rooms": None
        }
        return render(request, "echelon/index_rooms.html", context)


@login_required(login_url='login_user')
def create_room(request):
    if request.method == "POST":
        classes = request.POST["class"]
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        room = Room(
            title=title,
            is_active=is_active
        )
        room.save()
        room.class_fk.set(classes)
        return redirect("rooms")

    classes = Class.objects.all()
    context = {
        "classes": classes
    }
    return render(request, "echelon/edit_room.html", context)


@login_required(login_url='login_user')
def edit_room(request, pk):
    if request.method == "POST":
        classes = request.POST["class"]
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        room = Room.objects.get(id=pk)
        room.title = title
        room.is_active = is_active
        room.save()
        room.class_fk.set(classes)
        return redirect("rooms")

    room = Room.objects.get(id=pk)
    classes = Class.objects.all()
    context = {
        "classes": classes,
        "room": room
    }
    return render(request, "echelon/edit_room.html", context)


@login_required(login_url='login_user')
def delete_room(request, pk):
    Room.objects.get(id=pk).delete()
    return redirect('rooms')
