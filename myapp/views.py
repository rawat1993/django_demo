# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from myapp.models import Student, Course

# Create your views here.

@api_view(["GET","POST","PUT"])
def student_details(request):
    """
    Return the student details on the basis of roll number
    """
    
    if request.method=="GET":
        # requested_roll_number = request.query_params.get("roll_number")
        requested_roll_number = request.GET.get("roll_number")
        course = request.GET.get("course")
        
        if course:
            student_list = []
            student_queryset = Student.objects.filter(course__name=course)
            if not student_queryset:
                return Response(
                    {"message":"selected course does not have any student"},
                    status=status.HTTP_200_OK,
            )
            for obj in student_queryset:
                obj_dict = {}
                obj_dict["first_name"]=obj.first_name
                obj_dict["last_name"]=obj.last_name
                obj_dict["roll_number"]=obj.roll_number
                student_list.append(obj_dict)

            return Response(
                {"student_list":student_list},
                status=status.HTTP_200_OK,
            )

        if requested_roll_number:
            try:
                student_obj = Student.objects.get(roll_number=requested_roll_number)
            except Exception as error:
                return Response(
                    {"status":"failed","message":"User is not exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                {"first_name":student_obj.first_name,"father_name":student_obj.father_name,"course":student_obj.course.name},
                status=status.HTTP_200_OK,
            )
        
    if request.method=="POST":
        requested_data = request.data
        f_name = requested_data.get("student_first_name")
        l_name = requested_data.get("student_last_name","mbc")
        r_number = requested_data.get("roll_number")
        course = requested_data.get("course_name")

        try:
            couese_obj = Course.objects.get(name=course)
            Student.objects.create(first_name=f_name,last_name=l_name,roll_number=r_number,
                                course=couese_obj)

            return Response(
                {"status":"success","message":"User is created"},
                status=status.HTTP_201_CREATED
            )
        except Exception as error:
            print(error)
            return Response(
                {"status":"failed","message":"Course invalid"},
                status=status.HTTP_400_BAD_REQUEST
            )

    if request.method=="PUT":
        requested_data = request.data
        f_name = requested_data.get("student_first_name")
        l_name = requested_data.get("student_last_name","mbc")
        r_number = requested_data.get("roll_number")
        father_name = requested_data.get("father_name")
        mother_name = requested_data.get("mother_name")

        try:
            obj = Student.objects.get(roll_number=r_number)
            obj.first_name = f_name
            obj.last_name = l_name
            obj.father_name = father_name
            obj.mother_name = mother_name
            obj.save()

            return Response(
                {"status":"success","message":"User details are updated"},
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                {"status":"failed","message":"Student roll number is invalid"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
@api_view(["DELETE"])
def student_delete(request):

    if request.method=="DELETE":
        # import pdb; pdb.set_trace()
        requested_roll_number = request.query_params.get("roll_number")
        print(requested_roll_number,"roll number")
        try:
            Student.objects.get(roll_number=requested_roll_number).delete()
            return Response(
                {"status":"success","message":"User has been deleted"},
                status=status.HTTP_200_OK
            )
        except Exception as error:
            return Response(
                {"status":"failed","message":"Student roll number is invalid"},
                status=status.HTTP_400_BAD_REQUEST
            )