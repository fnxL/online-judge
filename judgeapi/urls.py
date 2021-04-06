
from django.contrib import admin
from django.urls import path
from judgeapi import views

urlpatterns = [
    path('<int:problem_id>', views.problem_page)
]
