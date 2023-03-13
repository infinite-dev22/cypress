from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from echelon.models import Class
from subject.models import Subject


# Permissions Views
@login_required(login_url='login_user')
def index_subjects(request):
    try:
        subjects = Subject.objects.all()

        context = {
            "subjects": subjects
        }
        return render(request, "subject/index_subjects.html", context)
    except ObjectDoesNotExist:
        context = {
            "subjects": None
        }
        return render(request, "subject/index_subjects.html", context)


@login_required(login_url='login_user')
def create_subject(request):
    if request.method == "POST":
        name = request.POST["name"]
        abbreviated_name = request.POST["abbreviated_name"]
        classes = request.POST.getlist("classes")
        is_active = request.POST.get("is_active", True) == 'on'
        is_optional = request.POST.get("is_optional", True) == 'on'
        subject = Subject(
            name=name,
            abbreviated_name=abbreviated_name,
            is_active=is_active,
            is_optional=is_optional
        )
        subject.save()
        subject.classes.set(classes)
        return redirect("subjects")
    classes = Class.objects.all()
    context = {
        "classes": classes,
    }
    return render(request, "subject/edit_subject.html", context)


@login_required(login_url='login_user')
def edit_subject(request, pk):
    if request.method == "POST":
        name = request.POST["name"]
        abbreviated_name = request.POST["abbreviated_name"]
        classes = request.POST.getlist("classes")
        is_active = request.POST.get("is_active", True) == 'on'
        is_optional = request.POST.get("is_optional", True) == 'on'
        subject = Subject.objects.get(id=pk)
        subject.name = name
        subject.abbreviated_name = abbreviated_name
        # subject.classes = classes
        subject.is_optional = is_optional
        subject.is_active = is_active
        subject.save()
        subject.classes.set(classes)
        return redirect("subjects")

    subject = Subject.objects.get(id=pk)
    classes = subject.classes.all()
    print(f"classes: {classes}")
    context = {
        "subject": subject,
        "classes": classes,
    }
    print(subject)
    return render(request, "subject/edit_subject.html", context)


@login_required(login_url='login_user')
def delete_subject(request, pk):
    Subject.objects.get(id=pk).delete()
    return redirect('subjects')
