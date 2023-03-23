from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Student
from myapp.serializers import StudentSerializer


class StudentViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving Students.
    """
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        data  = request.data
        # roll_num = data.get("roll_num")
        fname = data.get("father_name")

        Student.objects.filter(id=pk).update(father_name=fname)
        return Response({"status":"success","message":"Student father name updated"},
                        status=status.HTTP_200_OK)

