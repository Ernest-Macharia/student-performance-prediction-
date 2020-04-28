from django.db import models
from .studentprofile import StudentProfile


class Student(models.Model):
    __tablename__ = 'student'
    id = models.PositiveIntegerField(primary_key=True)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=128)
    created_date = models.DateTimeField(default=timezone.now)
    student_profile = models.OneToOneField(
        StudentProfile, on_delete=models.CASCADE)

    def get_id(self):
        return str(self.id)

    def __str__(self):
        return '<Student(fullname={} {})>'.format(self.firstname, self.lastname)
