from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation
from echelon.models import Level, Class
from grade.models import GradeMaster, GradeDetails
from subject.models import Subject


def index_grades(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            grades = GradeMaster.objects.all()
            context = {
                "grades": grades
            }
            return render(request, "admin_panel/grades/index_grades.html", context)
        except ObjectDoesNotExist:
            context = {
                "grades": None
            }
            return render(request, "admin_panel/grades/index_grades.html", context)
    return redirect('login_admin_user')


def create_grade(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            org_id = request.POST["organisation"]
            org = Organisation.objects.get(id=org_id)
            level_id = request.POST["level"]
            level = Level.objects.get(id=level_id)
            title = request.POST["title"]
            points = request.POST["points"]
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            grade = GradeMaster(
                organisation=org,
                level=level,
                title=title,
                point=points,
                is_active=is_active,
                description=description
            )
            grade.save()
            return redirect("admin_grades")

        orgs = Organisation.objects.all()
        level = Level.objects.all()
        context = {
            "orgs": orgs,
            "levels": level
        }

        return render(request, "admin_panel/grades/edit_grade.html", context)
    return redirect('login_admin_user')


def edit_grade(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            org_id = request.POST["organisation"]
            org = Organisation.objects.get(id=org_id)
            level_id = request.POST["level"]
            level = Level.objects.get(id=level_id)
            title = request.POST["title"]
            points = request.POST["points"]
            is_active = request.POST.get("is_active", False)
            description = request.POST["description"]
            grade = GradeMaster.objects.get(id=pk)
            grade.organisation = org
            grade.level = level
            grade.title = title
            grade.point = points
            grade.is_active = is_active
            grade.description = description
            grade.save()
            return redirect("admin_grades")

        grade = GradeMaster.objects.get(id=pk)
        orgs = Organisation.objects.all()
        level = Level.objects.all()
        context = {
            "grade": grade,
            "orgs": orgs,
            "levels": level
        }
        return render(request, "admin_panel/grades/edit_grade.html", context)
    return redirect('login_admin_user')


def delete_grade(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        GradeMaster.objects.get(id=pk).delete()
        return redirect("admin_grades")
    return redirect('login_admin_user')


def index_grade_details(request):
    if request.user.is_authenticated and request.user.is_superuser:
        try:
            grade_details = GradeDetails.objects.all()
            context = {
                "grade_details": grade_details
            }
            return render(request, "admin_panel/grades/index_grade_details.html", context)
        except ObjectDoesNotExist:
            context = {
                "grade_details": None
            }
            return render(request, "admin_panel/grades/index_grade_details.html", context)
    return redirect('login_admin_user')


def create_grade_detail(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            grade_id = request.POST["grade"]
            grade = GradeMaster.objects.get(id=grade_id)
            class_fk = request.POST.getlist("class")
            subject = request.POST.getlist("subject")
            marks_from = request.POST["marks_from"]
            marks_to = request.POST["marks_to"]
            is_active = request.POST.get("is_active", False)
            grade_detail = GradeDetails(
                grade=grade,
                marks_from=marks_from,
                marks_to=marks_to,
                is_active=is_active
            )
            grade_detail.save()
            grade_detail.class_fk.set(class_fk)
            grade_detail.subject.set(subject)
            return redirect("admin_grade_details")

        grades = GradeMaster.objects.all()
        classes = Class.objects.all()
        subjects = Subject.objects.all()
        context = {
            "grades": grades,
            "classes": classes,
            "subjects": subjects
        }

        return render(request, "admin_panel/grades/edit_grade_detail.html", context)
    return redirect('login_admin_user')


def edit_grade_detail(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            grade_id = request.POST["grade"]
            grade = GradeMaster.objects.get(id=grade_id)
            class_fk = request.POST.getlist("class")
            subject = request.POST.getlist("subject")
            marks_from = request.POST["marks_from"]
            marks_to = request.POST["marks_to"]
            is_active = request.POST.get("is_active", False)
            grade_detail = GradeDetails.objects.get(id=pk)
            grade_detail.grade = grade
            grade_detail.marks_from = marks_from
            grade_detail.marks_to = marks_to
            grade_detail.is_active = is_active
            grade_detail.save()
            grade_detail.class_fk.set(class_fk)
            grade_detail.subject.set(subject)
            return redirect("admin_grade_details")

        grade_detail = GradeDetails.objects.get(id=pk)
        grades = GradeMaster.objects.all()
        classes = Class.objects.all()
        subjects = Subject.objects.all()
        context = {
            "grade_detail": grade_detail,
            "grades": grades,
            "classes": classes,
            "subjects": subjects
        }
        return render(request, "admin_panel/grades/edit_grade_detail.html", context)
    return redirect('login_admin_user')


def delete_grade_detail(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        GradeDetails.objects.get(id=pk).delete()
        return redirect("admin_grade_details")
    return redirect('login_admin_user')
