from django.urls import path
from studentApp import views


urlpatterns = [

    path('', views.index, name="home"),
    path('register/', views.register, name="register"),
    path('', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('special/', views.special, name="special"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('registerstudent/', views.registerStudent, name="registerstudent"),
    path('get_students/', views.get_students, name="get_students"),
    path('getstudent/', views.get_student, name="get_student"),
    path('profile/', views.profile, name="profile"),
    path('comment/', views.feedback_form, name='comment'),
    path('student/', views.student, name='student'),
    path('admin/', views.admin, name='admin'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('feedback/', views.feedback, name="feedback"),


]
