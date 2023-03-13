import calendar
import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from assessment.models import Exam
from echelon.models import Class
from subject.models import Subject
from timetable.models import TimetableType, TimetableRecord, Timetable, TimeSlot

time_format = "%I::%M %p"


# Timetable Type
@login_required(login_url='login_user')
def index_timetable_type(request):
    try:
        timetable_types = TimetableType.objects.all()

        context = {
            "timetable_types": timetable_types
        }
        return render(request, "timetables/index_timetable_types.html", context)
    except ObjectDoesNotExist:
        context = {
            "timetable_types": None
        }
        return render(request, "timetables/index_timetable_types.html", context)


@login_required(login_url='login_user')
def create_timetable_type(request):
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
        return redirect("timetables_types")
    return render(request, "timetables/edit_timetable_types.html")


@login_required(login_url='login_user')
def edit_timetable_type(request, pk):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        # is_active = request.POST.get("is_active", False)
        timetable_type = TimetableType.objects.get(id=pk)
        timetable_type.title = title
        timetable_type.description = description
        # timetable_type.is_active = is_active
        timetable_type.save()
        return redirect("timetables_types")

    timetable_type = TimetableType.objects.get(id=pk)
    context = {
        "timetable_type": timetable_type,
    }
    return render(request, "timetables/edit_timetable_types.html", context)


@login_required(login_url='login_user')
def delete_timetable_type(request, pk):
    TimetableType.objects.get(id=pk).delete()
    return redirect('timetables_types')


# Timetable Records
@login_required(login_url='login_user')
def index_timetable_record(request):
    try:
        timetable_records = TimetableRecord.objects.all()

        context = {
            "timetable_records": timetable_records
        }
        return render(request, "timetables/index_timetable_records.html", context)
    except ObjectDoesNotExist:
        context = {
            "timetable_records": None
        }
        return render(request, "timetables/index_timetable_records.html", context)


@login_required(login_url='login_user')
def create_timetable_record(request):
    if request.method == "POST":
        event = request.POST["event"]
        time_slot_id = request.POST["time_slot"]
        time_slot = TimeSlot.objects.get(id=time_slot_id)
        day_of_week = request.POST["day_of_week"]
        # is_active = request.POST.get("is_active", False)
        timetable_record = TimetableRecord(
            event=event,
            time_slot=time_slot,
            day_of_week=day_of_week,
            # is_active=is_active,
        )
        timetable_record.save()
        return redirect("timetables_records")
    time_slots = TimeSlot.objects.all()
    week_days = calendar.day_name
    context = {
        "time_slots": time_slots,
        "week_days": week_days
    }
    return render(request, "timetables/edit_timetable_records.html", context)


@login_required(login_url='login_user')
def edit_timetable_record(request, pk):
    if request.method == "POST":
        event = request.POST["event"]
        time_slot_id = request.POST["time_slot"]
        time_slot = TimeSlot.objects.get(id=time_slot_id)
        day_of_week = request.POST["day_of_week"]
        # is_active = request.POST.get("is_active", False)
        timetable_record = TimetableRecord.objects.get(id=pk)
        timetable_record.event = event
        timetable_record.time_slot = time_slot
        timetable_record.day_of_week = day_of_week
        # timetable_record.is_active = is_active
        timetable_record.save()
        return redirect("timetables_records")

    timetable_record = TimetableRecord.objects.get(id=pk)
    time_slots = TimeSlot.objects.all()
    week_days = calendar.day_name
    context = {
        "time_slots": time_slots,
        "timetable_record": timetable_record,
        "week_days": week_days
    }
    return render(request, "timetables/edit_timetable_records.html", context)


@login_required(login_url='login_user')
def delete_timetable_record(request, pk):
    TimetableRecord.objects.get(id=pk).delete()
    return redirect('timetables_records')


# Time Slot
@login_required(login_url='login_user')
def index_time_slot(request):
    try:
        time_slots = TimeSlot.objects.all()

        context = {
            "time_slots": time_slots
        }
        return render(request, "timetables/index_time_slots.html", context)
    except ObjectDoesNotExist:
        context = {
            "time_slots": None
        }
        return render(request, "timetables/index_time_slots.html", context)


@login_required(login_url='login_user')
def create_time_slot(request):
    if request.method == "POST":
        hour_from = request.POST["hour_from"]
        minute_from = request.POST["minute_from"]
        meridian_from = request.POST["meridian_from"]
        hour_to = request.POST["hour_to"]
        minute_to = request.POST["minute_to"]
        meridian_to = request.POST["meridian_to"]

        time_from = f"{hour_from}::{minute_from} {meridian_from}"
        time_to = f"{hour_to}::{minute_to} {meridian_to}"
        time_from = datetime.datetime.strptime(time_from, time_format).time()
        time_to = datetime.datetime.strptime(time_to, time_format).time()
        # is_active = request.POST.get("is_active", False)
        time_slot = TimeSlot(
            hour_from=hour_from,
            minute_from=minute_from,
            meridian_from=meridian_from,
            hour_to=hour_to,
            minute_to=minute_to,
            meridian_to=meridian_to,
            timestamp_from=time_from,
            timestamp_to=time_to,
            # is_active=is_active,
        )
        time_slot.save()
        return redirect("time_slots")
    return render(request, "timetables/edit_time_slots.html")


@login_required(login_url='login_user')
def edit_time_slot(request, pk):
    if request.method == "POST":
        hour_from = request.POST["hour_from"]
        minute_from = request.POST["minute_from"]
        meridian_from = request.POST["meridian_from"]
        hour_to = request.POST["hour_to"]
        minute_to = request.POST["minute_to"]
        meridian_to = request.POST["meridian_to"]

        timestamp_from = f"{hour_from}::{minute_from} {meridian_from}"
        timestamp_to = f"{hour_to}::{minute_to} {meridian_to}"

        # is_active = request.POST.get("is_active", False)
        time_slot = TimeSlot.objects.get(id=pk)
        time_slot.hour_from = hour_from
        time_slot.minute_from = minute_from
        time_slot.meridian_from = meridian_from
        time_slot.hour_to = hour_to
        time_slot.minute_to = minute_to
        time_slot.meridian_to = meridian_to
        # time_slot.timestamp_from = time.strptime(timestamp_from, time_format),
        # time_slot.timestamp_to = time.strptime(timestamp_to, time_format),
        # time_slot.is_active = is_active
        time_slot.save()
        return redirect("time_slots")

    time_slot = TimeSlot.objects.get(id=pk)
    context = {
        "time_slot": time_slot,
    }
    return render(request, "timetables/edit_time_slots.html", context)


@login_required(login_url='login_user')
def delete_time_slot(request, pk):
    TimeSlot.objects.get(id=pk).delete()
    return redirect('time_slots')


# Timetable
@login_required(login_url='login_user')
def index_timetable(request):
    try:
        timetables = Timetable.objects.all()

        context = {
            "timetables": timetables
        }
        return render(request, "timetables/index_timetables.html", context)
    except ObjectDoesNotExist:
        context = {
            "timetables": None
        }
        return render(request, "timetables/index_timetables.html", context)


@login_required(login_url='login_user')
def create_timetable(request):
    if request.method == "POST":
        timetable_type_id = request.POST["timetable_type"]
        timetable_type = TimetableType.objects.get(id=timetable_type_id)
        class_fk = request.POST.getlist("class_ids")
        exam_id = request.POST["exam"]
        exam = Exam.objects.get(id=exam_id)
        subject = request.POST.getlist("subject")
        # is_active = request.POST.get("is_active", False)
        timetable = Timetable(
            timetable_type=timetable_type,
            exam=exam,
            # is_active=is_active,
        )
        timetable.save()
        timetable.class_fk.set(class_fk)
        timetable.subject.set(subject)
        return redirect("timetables")

    timetable_types = TimetableType.objects.all()
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    exams = Exam.objects.all()

    context = {
        "timetable_types": timetable_types,
        "classes": classes,
        "subjects": subjects,
        "exams": exams
    }
    return render(request, "timetables/edit_timetables.html", context)


@login_required(login_url='login_user')
def edit_timetable(request, pk):
    if request.method == "POST":
        timetable_type_id = request.POST["timetable_type"]
        timetable_type = TimetableType.objects.get(id=timetable_type_id)
        class_fk = request.POST.getlist("class_ids")
        exam_id = request.POST["exam"]
        exam = Exam.objects.get(id=exam_id)
        subject = request.POST.getlist("subject")
        timetable = Timetable.objects.get(id=pk)
        timetable.timetable_type = timetable_type
        timetable.exam = exam
        # timetable.is_active = is_active
        timetable.save()
        timetable.class_fk.set(class_fk)
        timetable.subject.set(subject)
        return redirect("timetables")

    timetable = Timetable.objects.get(id=pk)
    timetable_types = TimetableType.objects.all()
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    exams = Exam.objects.all()

    context = {
        "timetable_types": timetable_types,
        "classes": classes,
        "subjects": subjects,
        "exams": exams,
        "timetable": timetable,
    }
    return render(request, "timetables/edit_timetables.html", context)


@login_required(login_url='login_user')
def delete_timetable(request, pk):
    Timetable.objects.get(id=pk).delete()
    return redirect('timetables')
