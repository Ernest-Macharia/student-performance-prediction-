from django.contrib import admin


# Register your models here.
from studentApp.models import User, StudentProfile, Student, UserFeedbackModel

admin.site.register(User)
admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(UserFeedbackModel)
