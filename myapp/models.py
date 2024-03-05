from django.db import models


class Student(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    date_of_birth = models.DateField()

    class Meta:
        db_table = 'Wanafunzi'
