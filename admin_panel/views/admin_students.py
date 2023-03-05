from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render

from accounts.models.user import Student, User, UserType
from echelon.models import Class


# Permissions Views
def index_students(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            students = Student.objects.all()

            context = {
                "students": students
            }
            return render(request, "admin_panel/students/index_students.html", context)
        except ObjectDoesNotExist:
            context = {
                "students": None
            }
            return render(request, "admin_panel/students/index_students.html", context)
    return redirect('login_admin_user')


def create_student(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            middle_name = request.POST["middle_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            address = request.POST["address"]
            class_id = request.POST["class_id"]
            class_fk = Class.objects.get(id=class_id)
            # subjects = request.POST.getlist("subjects")
            parents = request.POST.getlist("parents")
            is_active = request.POST.get("is_active", True)
            is_staff = request.POST.get("is_active", False)
            student = Student(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                email=email,
                is_staff=is_staff,
                address=address,
                class_fk=class_fk,
                is_active=is_active
            )
            student.save()
            # student.subjects.set(subjects)
            student.parents.set(parents)
            return redirect("admin_student")

        # subjects = Subject.objects.all()
        classes = Class.objects.all()
        user_type = UserType.objects.filter(title='Parent')
        parents = User.objects.filter(user_type__in=user_type)  # Error here.
        context = {
            "classes": classes,
            # "subjects": subjects
            "parents": parents
        }
        return render(request, "admin_panel/students/edit_student.html", context)
    return redirect('login_admin_user')


def edit_student(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            middle_name = request.POST["middle_name"]
            last_name = request.POST["last_name"]
            is_active = request.POST.get("is_active", True)
            class_id = request.POST["class_id"]
            print(f"{first_name} {middle_name} {last_name}")
            class_fk = Class.objects.get(id=class_id)
            student = Student.objects.get(id=pk)
            student.first_name = first_name
            student.middle_name = middle_name
            student.last_name = last_name
            student.class_fk = class_fk
            student.is_active = is_active
            student.save()
            return redirect("admin_student")

        student = Student.objects.get(id=pk)
        classes = Class.objects.all()
        permissions = Permission.objects.all()
        context = {
            "classes": classes,
            "student": student,
            "permissions": permissions
        }
        return render(request, "admin_panel/students/edit_student.html", context)
    return redirect('login_admin_user')


def delete_student(request, pk):
    if request.user.is_authenticated:
        Student.objects.get(id=pk).delete()
        return redirect('admin_student')
    return redirect('login_admin_user')
