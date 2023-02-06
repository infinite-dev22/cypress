from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from accounts.models.user import Teacher, UserType
from echelon.models import Class
from subject.models import Subject


# Permissions Views
def index_teachers(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            teachers = Teacher.objects.all()

            context = {
                "teachers": teachers
            }
            return render(request, "admin_panel/teachers/index_teachers.html", context)
        except ObjectDoesNotExist:
            context = {
                "teachers": None
            }
            return render(request, "admin_panel/teachers/index_teachers.html", context)
    return redirect('login_admin_user')


def create_teacher(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            middle_name = request.POST["middle_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            telephone1 = request.POST["telephone1"]
            telephone2 = request.POST["telephone2"]
            email = request.POST["email"]
            address = request.POST["address"]
            subjects = request.POST.getlist("subjects")
            classes = request.POST.getlist("classes")
            is_active = request.POST.get("is_active", False)
            is_staff = request.POST.get("is_active", True)
            user_type = UserType.objects.filter(title='Teacher')
            teacher = Teacher(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                username=username,
                telephone1=telephone1,
                telephone2=telephone2,
                email=email,
                user_type=user_type,
                address=address,
                is_staff=is_staff,
                is_active=is_active
            )
            teacher.save()
            teacher.subject.set(subjects)
            teacher.school_class.set(classes)
            return redirect("admin_teacher")

        subjects = Subject.objects.all()
        classes = Class.objects.all()
        context = {
            "classes": classes,
            "subjects": subjects
        }
        return render(request, "admin_panel/teachers/edit_teacher.html", context)
    return redirect('login_admin_user')


def edit_teacher(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            middle_name = request.POST["middle_name"]
            last_name = request.POST["last_name"]
            username = request.POST["username"]
            telephone1 = request.POST["telephone1"]
            telephone2 = request.POST["telephone2"]
            email = request.POST["email"]
            address = request.POST["address"]
            subjects = request.POST.getlist("subjects")
            classes = request.POST.getlist("classes")
            is_active = request.POST.get("is_active", False)

            teacher = Teacher.objects.get(id=pk)
            teacher.first_name = first_name
            teacher.middle_name = middle_name
            teacher.last_name = last_name
            teacher.username = username
            teacher.telephone1 = telephone1
            teacher.telephone2 = telephone2
            teacher.email = email
            teacher.address = address
            teacher.school_class = classes
            teacher.subject = subjects
            teacher.is_active = is_active
            teacher.save()
            return redirect("admin_teacher")

        teacher = Teacher.objects.get(id=pk)
        subjects = Subject.objects.all()
        classes = Class.objects.all()
        context = {
            "classes": classes,
            "subjects": subjects,
            "teacher": teacher
        }
        return render(request, "admin_panel/teachers/edit_teacher.html", context)
    return redirect('login_admin_user')


def delete_teacher(request, pk):
    if request.user.is_authenticated:
        Teacher.objects.get(id=pk).delete()
        return redirect('admin_teacher')
    return redirect('login_admin_user')
