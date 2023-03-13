from django.urls import path

from users import views

USER_URLS = [
    # User Urls
    path('user/', views.index_user, name="users"),
    path('user/add/', views.create_user, name="user_add"),
    path('user/add/<int:pk>', views.edit_user, name="user_edit"),
    path('user/del/<int:pk>', views.delete_user, name="user_del"),
]

STUDENTS_URLS = [
    path('students/', views.index_students, name="students"),
    path('student/add/', views.create_student, name="student_add"),
    path('student/add/<int:pk>', views.edit_student, name="student_edit"),
    path('student/del/<int:pk>', views.delete_student, name="student_del"),
]

TEACHERS_URLS = [
    path('teachers/', views.index_teachers, name="teachers"),
    path('teacher/add/', views.create_teacher, name="teacher_add"),
    path('teacher/add/<int:pk>', views.edit_teacher, name="teacher_edit"),
    path('teacher/del/<int:pk>', views.delete_teacher, name="teacher_del"),
]

urlpatterns = USER_URLS \
              + STUDENTS_URLS \
              + TEACHERS_URLS
