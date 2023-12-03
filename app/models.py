from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Teacher(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    def __str__(self):
        return self.name