from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from timetable.models import TimetableType, TimetableRecord, Timetable, TimeSlot


# Timetable Type
def index_timetable_type(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            timetable_types = TimetableType.objects.all()

            context = {
                "timetable_types": timetable_types
            }
            return render(request, "admin_panel/timetables/index_timetable_types.html", context)
        except ObjectDoesNotExist:
            context = {
                "timetable_types": None
            }
            return render(request, "admin_panel/timetables/index_timetable_types.html", context)
    else:
        return redirect('login_admin_user')


def create_timetable_type(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable_type = TimetableType(
                title=title,
                # is_active=is_active,
                description=description
            )
            timetable_type.save()
            return redirect("admin_timetables_types")
        return render(request, "admin_panel/timetables/edit_timetable_types.html")
    else:
        return redirect('login_admin_user')


def edit_timetable_type(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable_type = TimetableType.objects.get(id=pk)
            timetable_type.title = title
            timetable_type.description = description
            # timetable_type.is_active = is_active
            timetable_type.save()
            return redirect("admin_timetables_types")

        timetable_type = TimetableType.objects.get(id=pk)
        context = {
            "timetable_type": timetable_type,
        }
        return render(request, "admin_panel/timetables/edit_timetable_types.html", context)
    else:
        return redirect('login_admin_user')


def delete_timetable_type(request, pk):
    if request.user.is_authenticated:
        TimetableType.objects.get(id=pk).delete()
        return redirect('admin_timetables_types')
    else:
        return redirect('login_admin_user')


# Timetable Records
def index_timetable_record(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            timetable_records = TimetableRecord.objects.all()

            context = {
                "timetable_records": timetable_records
            }
            return render(request, "admin_panel/timetables/index_timetable_records.html", context)
        except ObjectDoesNotExist:
            context = {
                "timetable_records": None
            }
            return render(request, "admin_panel/timetables/index_timetable_records.html", context)
    else:
        return redirect('login_admin_user')


def create_timetable_record(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable_record = TimetableRecord(
                title=title,
                # is_active=is_active,
                description=description
            )
            timetable_record.save()
            return redirect("admin_timetables_types")
        return render(request, "admin_panel/timetables/edit_timetable_records.html")
    else:
        return redirect('login_admin_user')


def edit_timetable_record(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable_record = TimetableRecord.objects.get(id=pk)
            timetable_record.title = title
            timetable_record.description = description
            # timetable_record.is_active = is_active
            timetable_record.save()
            return redirect("admin_timetables_types")

        timetable_record = TimetableRecord.objects.get(id=pk)
        context = {
            "timetable_record": timetable_record,
        }
        return render(request, "admin_panel/timetables/edit_timetable_records.html", context)
    else:
        return redirect('login_admin_user')


def delete_timetable_record(request, pk):
    if request.user.is_authenticated:
        TimetableRecord.objects.get(id=pk).delete()
        return redirect('admin_timetables_records')
    else:
        return redirect('login_admin_user')


# Time Slot
def index_time_slot(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            time_slots = TimeSlot.objects.all()

            context = {
                "time_slots": time_slots
            }
            return render(request, "admin_panel/timetables/index_time_slots.html", context)
        except ObjectDoesNotExist:
            context = {
                "time_slots": None
            }
            return render(request, "admin_panel/timetables/index_time_slots.html", context)
    else:
        return redirect('login_admin_user')


def create_time_slot(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            time_slot = TimeSlot(
                title=title,
                # is_active=is_active,
                description=description
            )
            time_slot.save()
            return redirect("admin_timetables_types")
        return render(request, "admin_panel/timetables/edit_time_slots.html")
    else:
        return redirect('login_admin_user')


def edit_time_slot(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            time_slot = TimeSlot.objects.get(id=pk)
            time_slot.title = title
            time_slot.description = description
            # time_slot.is_active = is_active
            time_slot.save()
            return redirect("admin_timetables_types")

        time_slot = TimeSlot.objects.get(id=pk)
        context = {
            "time_slot": time_slot,
        }
        return render(request, "admin_panel/timetables/edit_time_slots.html", context)
    else:
        return redirect('login_admin_user')


def delete_time_slot(request, pk):
    if request.user.is_authenticated:
        TimeSlot.objects.get(id=pk).delete()
        return redirect('admin_time_slots')
    else:
        return redirect('login_admin_user')


# Timetable
def index_timetable(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            timetables = Timetable.objects.all()

            context = {
                "timetables": timetables
            }
            return render(request, "admin_panel/timetables/index_timetables.html", context)
        except ObjectDoesNotExist:
            context = {
                "timetables": None
            }
            return render(request, "admin_panel/timetables/index_timetables.html", context)
    else:
        return redirect('login_admin_user')


def create_timetable(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable = Timetable(
                title=title,
                # is_active=is_active,
                description=description
            )
            timetable.save()
            return redirect("admin_timetables_types")
        return render(request, "admin_panel/timetables/edit_timetables.html")
    else:
        return redirect('login_admin_user')


def edit_timetable(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            title = request.POST["title"]
            description = request.POST["description"]
            # is_active = request.POST.get("is_active", False)
            timetable = Timetable.objects.get(id=pk)
            timetable.title = title
            timetable.description = description
            # timetable.is_active = is_active
            timetable.save()
            return redirect("admin_timetables_types")

        timetable = Timetable.objects.get(id=pk)
        context = {
            "timetable": timetable,
        }
        return render(request, "admin_panel/timetables/edit_timetables.html", context)
    else:
        return redirect('login_admin_user')


def delete_timetable(request, pk):
    if request.user.is_authenticated:
        Timetable.objects.get(id=pk).delete()
        return redirect('admin_timetables')
    else:
        return redirect('login_admin_user')
