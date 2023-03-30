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
    
    def update(self, request, pk=None):
        try:
            queryset = Student.objects.get(pk=pk)
            serializer_obj = StudentSerializer(queryset, data=request.data)
            # if Student.objects.get(serializer_obj.data['roll_number']):
            if serializer_obj.is_valid():
                serializer_obj.save()                  
                return Response(serializer_obj.data, status = status.HTTP_200_OK)
        except Exception as error:
            return Response({"status": "failed", "message":"pk not found!"}, status=status.HTTP_404_NOT_FOUND)
 
    def partial_update(self, request, pk=None):
        try:
            queryset = Student.objects.get(pk=pk)
            serializer_obj = StudentSerializer(queryset, data=request.data, partial=True)
            if serializer_obj.is_valid():
                serializer_obj.save() 
                return Response(serializer_obj.data, status = status.HTTP_206_PARTIAL_CONTENT)
            
        except Exception as error:
            return Response({"status": "failed", "message":"pk not found!!"}, status=status.HTTP_404_NOT_FOUND)
            
    def destroy(self, request, pk=None):
        student = Student.objects.get(pk=pk).delete()
        return Response({"status": "success", "message":"student Deleted"}, status=status.HTTP_200_OK)
        
        
    def create(self, request):
        serializer_obj = StudentSerializer(data=request.data)
        try:
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
        except Exception as error:
            return Response({"status":"failed", "error":str(error)}, status=status.HTTP_400_BAD_REQUEST)
            
    def retrieve(self, request, pk=None):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({"status":"failed", "message":"pk is not found!"}, status=status.HTTP_404_NOT_FOUND)
            
            
            
            
            
            
            
            
