from django.db import models

# models
from core.models import Person


class Student(Person):
    registration = models.IntegerField(default=0)
    curso = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Estudante'
        verbose_name_plural = 'Estudantes'
