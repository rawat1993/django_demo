from django.contrib import admin

# Register your models here.
from myapp import models

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    """This is to represent prescription admin"""
    search_fields = ("first_name", "roll_number")
    list_display = (
        "first_name", "last_name", "father_name",
        "date_of_joining", "roll_number","created","modified","course")

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("name", "course_id")
    list_display = (
        "name", "course_id")