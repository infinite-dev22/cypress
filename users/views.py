from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

from accounts.models.user import Student, User, UserType, Teacher
from echelon.models import Class
from subject.models import Subject


# Students Views
@login_required(login_url='login_user')
def index_students(request):
    try:
        students = Student.objects.all()

        context = {
            "students": students
        }
        return render(request, "users/students/index_students.html", context)
    except ObjectDoesNotExist:
        context = {
            "students": None
        }
        return render(request, "users/students/index_students.html", context)


@login_required(login_url='login_user')
def create_student(request):
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
            organisation=request.user.organisation,
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
        return redirect("students")

    # subjects = Subject.objects.all()
    classes = Class.objects.all()
    user_type = UserType.objects.filter(title='Parent')
    parents = User.objects.filter(user_type__in=user_type)  # Error here.
    context = {
        "classes": classes,
        # "subjects": subjects
        "parents": parents
    }
    return render(request, "users/students/edit_student.html", context)


@login_required(login_url='login_user')
def edit_student(request, pk):
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
        return redirect("students")

    student = Student.objects.get(id=pk)
    classes = Class.objects.all()
    permissions = Permission.objects.all()
    context = {
        "classes": classes,
        "student": student,
        "permissions": permissions
    }
    return render(request, "users/students/edit_student.html", context)


@login_required(login_url='login_user')
def delete_student(request, pk):
    Student.objects.get(id=pk).delete()
    return redirect('student')


# Permissions Views
@login_required(login_url='login_user')
def index_teachers(request):
    try:
        teachers = Teacher.objects.all()

        context = {
            "teachers": teachers
        }
        return render(request, "users/teachers/index_teachers.html", context)
    except ObjectDoesNotExist:
        context = {
            "teachers": None
        }
        return render(request, "users/teachers/index_teachers.html", context)


@login_required(login_url='login_user')
def create_teacher(request):
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
        user_type = UserType.objects.get(title='Teacher')
        teacher = Teacher(
            organisation=request.user.organisation,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            username=username,
            telephone_1=telephone1,
            telephone_2=telephone2,
            email=email,
            user_type=user_type,
            address=address,
            is_staff=is_staff,
            is_active=is_active
        )
        teacher.save()
        teacher.subject.set(subjects)
        teacher.school_class.set(classes)
        return redirect("teachers")

    subjects = Subject.objects.all()
    classes = Class.objects.all()
    context = {
        "classes": classes,
        "subjects": subjects
    }
    return render(request, "users/teachers/edit_teacher.html", context)


@login_required(login_url='login_user')
def edit_teacher(request, pk):
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
        teacher.telephone_1 = telephone1
        teacher.telephone_2 = telephone2
        teacher.email = email
        teacher.address = address
        teacher.is_active = is_active
        teacher.save()
        teacher.subject.set(subjects)
        teacher.school_class.set(classes)
        return redirect("teachers")

    teacher = Teacher.objects.get(id=pk)
    subjects = Subject.objects.all()
    classes = Class.objects.all()
    context = {
        "classes": classes,
        "subjects": subjects,
        "teacher": teacher
    }
    return render(request, "users/teachers/edit_teacher.html", context)


@login_required(login_url='login_user')
def delete_teacher(request, pk):
    Teacher.objects.get(id=pk).delete()
    return redirect('teachers')


# User Views
@login_required(login_url='login_user')
def index_user(request):
    try:
        users = User.objects.all()

        context = {
            "users": users
        }
        return render(request, "users/users/index_user.html", context)
    except ObjectDoesNotExist:
        context = {
            "users": None
        }
        return render(request, "users/users/index_user.html", context)


@login_required(login_url='login_user')
def create_user(request):
    if request.method != 'POST':
        user_types = UserType.objects.all()
        context = {
            "user_types": user_types
        }
        return render(request, 'users/users/create_user.html', context)
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        user_type_id = request.POST['user_type']
        user_type = UserType.objects.get(id=user_type_id)
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(request, "username taken...")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.info(request, "email taken...")
            return redirect('admin_user')
        user = User.objects.create_user(
            organisation=request.user.organisation,
            username=username,
            password=password1,
            email=email,
            first_name=first_name,
            middle_name=middle_name,
            user_type=user_type,
            last_name=last_name
        )
        user.save()
        messages.info(request, "your account has been created successfully")
        return redirect('users')
    messages.info(request, "passwords do not match...")
    return redirect('user_add')


@login_required(login_url='login_user')
def edit_user(request, pk):
    if request.method != 'POST':
        user_types = UserType.objects.all()
        account = User.objects.get(id=pk)
        context = {
            "account": account,
            "user_types": user_types
        }
        return render(request, 'users/users/create_user.html', context)
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if password1 == password2:
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        user_type_id = request.POST['user_type']
        user_type = UserType.objects.get(id=user_type_id)  # Error here.
        email = request.POST['email']
        user = User.objects.get(id=pk)
        user.username = username,
        user.password = password1,
        user.email = email,
        user.first_name = first_name,
        user.middle_name = middle_name,
        user.user_type = user_type,
        user.last_name = last_name
        user.save()
        messages.info(request, "your account details have been updated successfully")
        return redirect('users')
    messages.info(request, "passwords do not match...")
    return redirect('user_add')


@login_required(login_url='login_user')
def delete_user(request, pk):
    User.objects.get(id=pk).delete()
    return redirect('users')


def get_image_html(url):
    return format_html(
        '<a target="_blank" href="{0}">'
        '<div style="background-image: url(\'{0}\'); '
        'background-position: center; height: 100px; width: 100px; background-size: cover"></div>'
        '</a>'.format(url))


def format_picture(item):
    if item.profile_pic:
        thumbnail = get_thumbnail(item.profile_pic, '200x200', crop='center', quality=99)
        return get_image_html(thumbnail.url)
