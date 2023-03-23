from django.db import models

# Create your models here.
from datetime import date

# Register your models here.
class Course(models.Model):
    """A class to represent Student details model"""
    name = models.CharField(max_length=50)
    course_id = models.CharField(max_length=20, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """This is the method to represent name as string"""
        return self.name

class Student(models.Model):
    """A class to represent Student details model"""
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    mother_name = models.CharField(max_length=50,null=True, blank=True)
    date_of_joining = models.DateField(default=date.today)
    roll_number = models.PositiveIntegerField(default=1)

    course = models.ForeignKey(Course,on_delete=models.SET_NULL, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """This is the method to represent name as string"""
        return self.first_name
