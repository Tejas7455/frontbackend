from rest_framework import viewsets
from .serializers import EmployeeSerializers
from .models import Employee

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()