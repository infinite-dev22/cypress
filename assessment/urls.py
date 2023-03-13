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

from assessment import views

EXAM_TYPES_URLS = [
    path('assessments/exam_type/', views.index_exam_types, name="exam_types"),
    path('assessments/exam_type/add/', views.create_exam_type, name="exam_type_add"),
    path('assessments/exam_type/add/<int:pk>', views.edit_exam_type, name="exam_type_edit"),
    path('assessments/exam_type/del/<int:pk>', views.delete_exam_type, name="exam_type_del"),
]

EXAMS_URLS = [
    path('assessments/exam/', views.index_exams, name="exams"),
    path('assessments/exam/add/', views.create_exam, name="exam_add"),
    path('assessments/exam/add/<int:pk>', views.edit_exam, name="exam_edit"),
    path('assessments/exam/del/<int:pk>', views.delete_exam, name="exam_del"),
]

EXAM_RESULTS_URLS = [
    path('assessments/result/', views.index_results, name="results"),
    path('assessments/result/add/', views.create_result, name="result_add"),
    path('assessments/result/add/<int:pk>', views.edit_result, name="result_edit"),
    path('assessments/result/del/<int:pk>', views.delete_result, name="result_del"),
]

EXAM_SCORES_URLS = [
    path('assessments/score/', views.index_scores, name="scores"),
    path('assessments/score/add/', views.create_score, name="score_add"),
    path('assessments/score/add/<int:pk>', views.edit_score, name="score_edit"),
    path('assessments/score/del/<int:pk>', views.delete_score, name="score_del")
]

urlpatterns = EXAM_TYPES_URLS \
              + EXAMS_URLS \
              + EXAM_RESULTS_URLS \
              + EXAM_SCORES_URLS
