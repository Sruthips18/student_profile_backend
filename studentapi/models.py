from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.CharField(maz_length=100)
    parent_name=models.CharField(max_length=100)
    parent_num=models.CharField(max_length=100)
    guard_relation=models.CharField(max_length=100)

    def __str__(self):
        return self.name