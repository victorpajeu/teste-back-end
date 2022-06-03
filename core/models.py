from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, null=False)
    idade = models.IntegerField(default=1)
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    class Meta:
        abstract = True
