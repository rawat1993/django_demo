from rest_framework import serializers
from myapp.models import Course, Student

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['name', 'course_id']

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'father_name', 'roll_number']