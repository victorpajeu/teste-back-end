from rest_framework import serializers


# models
from students.models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'idade', 'registration', 'curso', 'created_at', 'updated_at']

