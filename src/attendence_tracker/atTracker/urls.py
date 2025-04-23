from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("st/<int:id>/", views.student, name="student"),
    path("add_student/", views.add_student, name="add_student")
]