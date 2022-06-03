from rest_framework import viewsets

# models
from students.models import Student

# serializers
from students.api.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


