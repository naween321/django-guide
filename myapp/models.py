from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return f"This object is {self.name}"


class Experience(models.Model):
    designation = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

