from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Course
from myapp.serializers import CourseSerializer

class CourseList(APIView):

    def get(self,request):
        course_queryset = Course.objects.all()
        serializer_obj = CourseSerializer(course_queryset,many=True)
        return Response(serializer_obj.data,status=status.HTTP_200_OK)

class AddCourse(APIView):

    def post(self,request):
        data = request.data
        couse_name = data.get("name")
        course_id = data.get("course_id")
        Course.objects.create(name=couse_name,course_id=course_id)
        return Response({"status":"success","message":"course added"},status=status.HTTP_201_CREATED)

class UpdateCourse(APIView):

    def put(self, request, pk):
        try:
            course_obj = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({"status":"failed","error":str(error)}, status=status.HTTP_404_NOT_FOUND)

class DeleteCourse(APIView):

    def delete(self, request, pk):
        try:
            Course.objects.get(pk=pk).delete()
            return Response({"status":"success","message":"Course deleted"},status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"status":"failed","error":str(error)}, status=status.HTTP_404_NOT_FOUND)

