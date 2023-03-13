"""cypress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from admin_panel.views import admin_users, admin_organisation, admin_roles, admin_user_types, admin_dashboard, \
    admin_echelon, admin_students, admin_teachers, admin_terms, admin_subjects, admin_chats, admin_timetables, \
    admin_grades, admin_assessments

DASHBOARD_URLS = [
    path('', admin_dashboard.dashboard_admin, name="admin_dashboard"),
]

ORGANISATION_URLS = [
    path('organisation/', admin_organisation.index_organisation, name="admin_org"),
    path('organisation/profiles', admin_organisation.index_organisation_profile, name="admin_org_profiles"),
    path('organisation/add/', admin_organisation.create_organisation, name="org_add"),
    path('organisation/add/<int:pk>', admin_organisation.edit_organisation, name="org_edit"),
    path('organisation/del/<int:pk>', admin_organisation.delete_org, name="org_del"),
]

CONTROLS_URLS = [
    path('role/', admin_roles.index_roles, name="admin_role"),
    path('role/add/', admin_roles.create_role, name="role_add"),
    path('role/add/<int:pk>', admin_roles.edit_role, name="role_edit"),
    path('role/del/<int:pk>', admin_roles.delete_roles, name="role_del"),
]

USER_URLS = [
    # UserType Urls
    path('user_type/', admin_user_types.index_user_type, name="admin_user_type"),
    path('user_type/add/', admin_user_types.create_user_type, name="user_type_add"),
    path('user_type/add/<int:pk>', admin_user_types.edit_user_type, name="user_type_edit"),
    path('user_type/del/<int:pk>', admin_user_types.delete_user_type, name="user_type_del"),

    # User Urls
    path('user/', admin_users.index_base_user, name="admin_user"),
    path('user/add/', admin_users.create_user, name="admin_user_add"),
    path('user/add/<int:pk>', admin_users.edit_user, name="admin_user_edit"),
    path('user/del/<int:pk>', admin_users.delete_user, name="admin_user_del"),
    path('login/', admin_users.login, name="login_admin_user"),
    path('logout/', admin_users.logout, name="admin_user_logout"),
]

LEVELS_URLS = [
    path('level/', admin_echelon.index_levels, name="admin_level"),
    path('level/add/', admin_echelon.create_level, name="level_add"),
    path('level/add/<int:pk>', admin_echelon.edit_level, name="level_edit"),
    path('level/del/<int:pk>', admin_echelon.delete_level, name="level_del"),
]

TERMS_URLS = [
    path('terms/', admin_terms.index_terms, name="admin_term"),
    path('term/add/', admin_terms.create_term, name="term_add"),
    path('term/add/<int:pk>', admin_terms.edit_term, name="term_edit"),
    path('term/del/<int:pk>', admin_terms.delete_term, name="term_del"),
]

CLASSES_URLS = [
    path('class/', admin_echelon.index_classes, name="admin_class"),
    path('class/add/', admin_echelon.create_class, name="class_add"),
    path('class/add/<int:pk>', admin_echelon.edit_class, name="class_edit"),
    path('class/del/<int:pk>', admin_echelon.delete_class, name="class_del"),
]

ROOMS_URLS = [
    path('room/', admin_echelon.index_rooms, name="admin_room"),
    path('room/add/', admin_echelon.create_room, name="room_add"),
    path('room/add/<int:pk>', admin_echelon.edit_room, name="room_edit"),
    path('room/del/<int:pk>', admin_echelon.delete_room, name="room_del"),
]

SUBJECTS_URLS = [
    path('subjects/', admin_subjects.index_subjects, name="admin_subject"),
    path('subject/add/', admin_subjects.create_subject, name="subject_add"),
    path('subject/add/<int:pk>', admin_subjects.edit_subject, name="subject_edit"),
    path('subject/del/<int:pk>', admin_subjects.delete_subject, name="subject_del"),
]

TEACHERS_URLS = [
    path('teachers/', admin_teachers.index_teachers, name="admin_teacher"),
    path('teacher/add/', admin_teachers.create_teacher, name="teacher_add"),
    path('teacher/add/<int:pk>', admin_teachers.edit_teacher, name="teacher_edit"),
    path('teacher/del/<int:pk>', admin_teachers.delete_teacher, name="teacher_del"),
]

STUDENTS_URLS = [
    path('students/', admin_students.index_students, name="admin_student"),
    path('student/add/', admin_students.create_student, name="student_add"),
    path('student/add/<int:pk>', admin_students.edit_student, name="student_edit"),
    path('student/del/<int:pk>', admin_students.delete_student, name="student_del"),
]

CHATS_URLS = [
    path('chat/', admin_chats.index_chats, name="admin_chat"),
    path('chat/details/<int:pk>', admin_chats.chat_details, name="chat_details"),
]

TIMETABLES_URLS = [
    # Timetable Types
    path('timetables/types/', admin_timetables.index_timetable_type, name="admin_timetables_types"),
    path('timetables/types/create/', admin_timetables.create_timetable_type, name="timetables_type_add"),
    path('timetables/types/<int:pk>', admin_timetables.edit_timetable_type, name="timetable_type_edit"),
    path('timetables/types/del/<int:pk>', admin_timetables.delete_timetable_type, name="timetable_type_del"),
    # Timetable Records
    path('timetables/records/', admin_timetables.index_timetable_record, name="admin_timetables_records"),
    path('timetables/records/create/', admin_timetables.create_timetable_record, name="timetables_record_add"),
    path('timetables/records/<int:pk>', admin_timetables.edit_timetable_record, name="timetable_record_edit"),
    path('timetables/records/del/<int:pk>', admin_timetables.delete_timetable_record, name="timetable_record_del"),
    # Time Slots
    path('timetables/slots/', admin_timetables.index_time_slot, name="admin_time_slots"),
    path('timetables/slots/create/', admin_timetables.create_time_slot, name="time_slot_add"),
    path('timetables/slots/<int:pk>', admin_timetables.edit_time_slot, name="time_slot_edit"),
    path('timetables/slots/del/<int:pk>', admin_timetables.delete_time_slot, name="time_slot_del"),
    # Timetables
    path('timetables/', admin_timetables.index_timetable, name="admin_timetables"),
    path('timetables/create/', admin_timetables.create_timetable, name="timetable_add"),
    path('timetables/<int:pk>', admin_timetables.edit_timetable, name="timetable_edit"),
    path('timetables/del/<int:pk>', admin_timetables.delete_timetable, name="timetable_del"),
]

GRADES_URLS = [
    # Grades
    path('grades/', admin_grades.index_grades, name="admin_grades"),
    path('grades/create/', admin_grades.create_grade, name="grade_add"),
    path('grades/<int:pk>', admin_grades.edit_grade, name="grade_edit"),
    path('grades/del/<int:pk>', admin_grades.delete_grade, name="grade_del"),
    # Grade Details
    path('grades/details/', admin_grades.index_grade_details, name="admin_grade_details"),
    path('grades/details/create/', admin_grades.create_grade_detail, name="grade_detail_add"),
    path('grades/details/<int:pk>', admin_grades.edit_grade_detail, name="grade_detail_edit"),
    path('grades/details/del/<int:pk>', admin_grades.delete_grade_detail, name="grade_detail_del"),
]

EXAMS_URLS = [
    # Exam Types
    path('assessments/exam_type/', admin_assessments.index_exam_types, name="admin_exam_types"),
    path('assessments/exam_type/add/', admin_assessments.create_exam_type, name="exam_type_add"),
    path('assessments/exam_type/add/<int:pk>', admin_assessments.edit_exam_type, name="exam_type_edit"),
    path('assessments/exam_type/del/<int:pk>', admin_assessments.delete_exam_type, name="exam_type_del"),
    # Exams
    path('assessments/exam/', admin_assessments.index_exams, name="admin_exams"),
    path('assessments/exam/add/', admin_assessments.create_exam, name="exam_add"),
    path('assessments/exam/add/<int:pk>', admin_assessments.edit_exam, name="exam_edit"),
    path('assessments/exam/del/<int:pk>', admin_assessments.delete_exam, name="exam_del"),
    # Exam Results
    path('assessments/result/', admin_assessments.index_results, name="admin_results"),
    path('assessments/result/add/', admin_assessments.create_result, name="result_add"),
    path('assessments/result/add/<int:pk>', admin_assessments.edit_result, name="result_edit"),
    path('assessments/result/del/<int:pk>', admin_assessments.delete_result, name="result_del"),
    # Exam Scores
    path('assessments/score/', admin_assessments.index_scores, name="admin_scores"),
    path('assessments/score/add/', admin_assessments.create_score, name="score_add"),
    path('assessments/score/add/<int:pk>', admin_assessments.edit_score, name="score_edit"),
    path('assessments/score/del/<int:pk>', admin_assessments.delete_score, name="score_del")
]

urlpatterns = DASHBOARD_URLS \
              + ORGANISATION_URLS \
              + CONTROLS_URLS \
              + USER_URLS \
              + LEVELS_URLS \
              + TERMS_URLS \
              + CLASSES_URLS \
              + ROOMS_URLS \
              + SUBJECTS_URLS \
              + TEACHERS_URLS \
              + STUDENTS_URLS \
              + CHATS_URLS \
              + TIMETABLES_URLS \
              + GRADES_URLS \
              + EXAMS_URLS
