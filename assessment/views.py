import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect

from accounts.models.organisation import Organisation
from accounts.models.user import Student
from assessment.models import ExamType, Exam, Result, Score
from echelon.models import Class, Room, Term
from grade.models import GradeMaster
from subject.models import Subject


@login_required(login_url='login_user')
def index_exam_types(request):
    try:
        exam_types = ExamType.objects.all()
        context = {
            "exam_types": exam_types
        }
        return render(request, "assessments/index_exam_type.html", context)
    except ObjectDoesNotExist:
        context = {
            "exam_types": None
        }
        return render(request, "assessments/index_exam_type.html", context)


@login_required(login_url='login_user')
def create_exam_type(request):
    if request.method == "POST":
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        description = request.POST["description"]
        exam = ExamType(
            organisation=request.user.organisation,
            title=title,
            is_active=is_active,
            description=description
        )
        exam.save()
        return redirect("exam_types")

    orgs = Organisation.objects.all()
    context = {
        "orgs": orgs
    }

    return render(request, "assessments/edit_exam_type.html", context)


@login_required(login_url='login_user')
def edit_exam_type(request, pk):
    if request.method == "POST":
        org_id = request.POST["organisation"]
        org = Organisation.objects.get(id=org_id)
        title = request.POST["title"]
        is_active = request.POST.get("is_active", True)
        description = request.POST["description"]
        exam = ExamType.objects.get(id=pk)
        exam.organisation = org
        exam.title = title
        exam.is_active = is_active
        exam.description = description
        exam.save()
        return redirect("exam_types")

    exam = ExamType.objects.get(id=pk)
    orgs = Organisation.objects.all()
    context = {
        "exam_type": exam,
        "orgs": orgs
    }
    return render(request, "assessments/edit_exam_type.html", context)


@login_required(login_url='login_user')
def delete_exam_type(request, pk):
    ExamType.objects.get(id=pk).delete()
    return redirect("exam_types")


@login_required(login_url='login_user')
def index_exams(request):
    try:
        exam_masters = Exam.objects.all()
        context = {
            "exam_masters": exam_masters
        }
        return render(request, "assessments/index_exam_master.html", context)
    except ObjectDoesNotExist:
        context = {
            "exam_masters": None
        }
        return render(request, "assessments/index_exam_master.html", context)


@login_required(login_url='login_user')
def create_exam(request):
    if request.method == "POST":
        exam_type_id = request.POST["exam_type_id"]
        classes = request.POST.getlist("class_id")
        exam_type = ExamType.objects.get(id=exam_type_id)
        title = request.POST["title"]
        term_id = request.POST["term"]
        term = Term.objects.get(id=term_id)
        year = request.POST["year"]
        is_active = request.POST.get("is_active", True)
        # description = request.POST["description"]
        exam = Exam(
            exam_type=exam_type,
            title=title,
            term=term,
            year=year,
            is_active=is_active,
            # description=description
        )
        exam.save()
        exam.classes.set(classes)
        return redirect("exams")

    exam_types = ExamType.objects.all()
    terms = Term.objects.all()
    classes = Class.objects.all()
    context = {
        "exam_types": exam_types,
        "terms": terms,
        "classes": classes
    }

    return render(request, "assessments/edit_exam_master.html", context)


@login_required(login_url='login_user')
def edit_exam(request, pk):
    if request.method == "POST":
        exam_type_id = request.POST["exam_type_id"]
        classes = request.POST.getlist("class_id")
        exam_type = ExamType.objects.get(id=exam_type_id)
        title = request.POST["title"]
        term_id = request.POST["term"]
        term = Term.objects.get(id=term_id)
        year = request.POST["year"]
        is_active = request.POST.get("is_active", True)
        # description = request.POST["description"]
        exam = Exam.objects.get(id=pk)
        exam.exam_type = exam_type
        exam.title = title
        exam.term = term
        exam.year = year
        exam.is_active = is_active
        # exam.description = description
        exam.save()
        exam.classes.set(classes)
        return redirect("exams")

    terms = Term.objects.all()
    classes = Class.objects.all()
    exam = Exam.objects.get(id=pk)
    exam_types = ExamType.objects.all()
    context = {
        "exam": exam,
        "exam_types": exam_types,
        "terms": terms,
        "classes": classes
    }
    return render(request, "assessments/edit_exam_master.html", context)


@login_required(login_url='login_user')
def delete_exam(request, pk):
    Exam.objects.get(id=pk).delete()
    return redirect("exams")


@login_required(login_url='login_user')
def index_results(request):
    try:
        results = Result.objects.all()
        context = {
            "results": results
        }
        return render(request, "assessments/index_exam_results.html", context)
    except ObjectDoesNotExist:
        context = {
            "results": None
        }
        return render(request, "assessments/index_exam_results.html", context)


@login_required(login_url='login_user')
def create_result(request):
    if request.method == "POST":
        exam_id = request.POST["exam_id"]
        exam = Exam.objects.get(id=exam_id)
        student_id = request.POST["student_id"]
        student = Student.objects.get(id=student_id)
        class_id = request.POST["class_id"]
        class_fk = Class.objects.get(id=class_id)
        room_id = request.POST["room_id"]
        room = Room.objects.get(id=room_id)
        # is_active = request.POST.get("is_active", False)
        exam = Result(
            exam=exam,
            student=student,
            class_fk=class_fk,
            room=room
        )
        exam.save()
        return redirect("results")

    students = Student.objects.all()
    exams = Exam.objects.all()
    classes = Class.objects.all()
    rooms = Room.objects.all()
    context = {
        "students": students,
        "exams": exams,
        "classes": classes,
        "rooms": rooms,
    }

    return render(request, "assessments/edit_exam_result.html", context)


@login_required(login_url='login_user')
def edit_result(request, pk):
    if request.method == "POST":
        exam_id = request.POST["exam_id"]
        exam = Exam.objects.get(id=exam_id)
        class_id = request.POST["class_id"]
        class_fk = Class.objects.get(id=class_id)
        # student_slug = request.POST["student"]
        # student = BaseUser.objects.get(slug=student_slug)
        room_id = request.POST["room_id"]
        room = Room.objects.get(id=room_id)
        # is_active = request.POST.get("is_active", False)
        result = Result.objects.get(id=pk)
        result.exam = exam
        result.class_fk = class_fk
        result.room = room
        # result.student = student
        # result.is_active = is_active
        result.save()
        return redirect("results")

    result = Result.objects.get(id=pk)
    exams = Exam.objects.all()
    classes = Class.objects.all()
    subjects = Subject.objects.all()
    rooms = Room.objects.all()
    context = {
        "result": result,
        "exams": exams,
        "classes": classes,
        "subjects": subjects,
        "rooms": rooms
    }
    return render(request, "assessments/edit_exam_result.html", context)


@login_required(login_url='login_user')
def delete_result(request, pk):
    Result.objects.get(id=pk).delete()
    return redirect("results")


@login_required(login_url='login_user')
def index_scores(request):
    try:
        scores = Score.objects.all()
        context = {
            "scores": scores
        }
        return render(request, "assessments/index_exam_scores.html", context)
    except ObjectDoesNotExist:
        context = {
            "scores": None
        }
        return render(request, "assessments/index_exam_scores.html", context)


@login_required(login_url='login_user')
def create_score(request):
    if request.method == "POST":
        result_id = request.POST["result_id"]
        result = Result.objects.get(id=result_id)
        subject_id = request.POST["subject_id"]
        subject = Subject.objects.get(id=subject_id)
        grade_id = request.POST["grade_id"]
        grade = GradeMaster.objects.get(id=grade_id)
        test_score = request.POST["test_score"]
        # year = request.POST["year"]
        # is_active = request.POST.get("is_active", False)
        score = Score(
            exam_result=result,
            subject=subject,
            grade=grade,
            test_score=test_score,
            year=int(datetime.datetime.now().year)
        )
        score.save()
        return redirect("scores")

    grades = GradeMaster.objects.all()
    results = Result.objects.all()
    subjects = Subject.objects.all()
    context = {
        "grades": grades,
        "results": results,
        "subjects": subjects
    }

    return render(request, "assessments/edit_exam_score.html", context)


@login_required(login_url='login_user')
def edit_score(request, pk):
    if request.method == "POST":
        result_id = request.POST["result_id"]
        result = Result.objects.get(id=result_id)
        subject_id = request.POST["subject_id"]
        subject = Subject.objects.get(id=subject_id)
        grade_id = request.POST["grade_id"]
        grade = GradeMaster.objects.get(id=grade_id)
        test_score = request.POST["test_score"]
        # is_active = request.POST.get("is_active", False)
        score = Score.objects.get(id=pk)
        score.result = result
        score.subject = subject
        score.grade = grade
        score.exam_result = result
        score.test_score = test_score
        score.year = int(datetime.datetime.now().year)
        score.save()
        return redirect("scores")

    score = Score.objects.get(id=pk)
    grades = GradeMaster.objects.all()
    results = Result.objects.all()
    subjects = Subject.objects.all()
    context = {
        "score": score,
        "grades": grades,
        "results": results,
        "subjects": subjects
    }
    return render(request, "assessments/edit_exam_score.html", context)


@login_required(login_url='login_user')
def delete_score(request, pk):
    Score.objects.get(id=pk).delete()
    return redirect("scores")
