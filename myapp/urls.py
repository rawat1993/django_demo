from django.urls import path
from myapp import views

urlpatterns = [
    path("details/", views.student_details, name="student-details"),
    path("remove-student/", views.student_delete, name="student-delete"),
]