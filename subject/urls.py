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

from subject import views

urlpatterns = [
    path('subjects/', views.index_subjects, name="subjects"),
    path('subject/add/', views.create_subject, name="subject_add"),
    path('subject/add/<int:pk>', views.edit_subject, name="subject_edit"),
    path('subject/del/<int:pk>', views.delete_subject, name="subject_del"),
]
