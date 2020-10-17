
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from studentApp.forms import SignUpForm, UserFeedbackForm, StudentForm, StudentProfileForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from studentApp.serializers import UserSchema, StudentSchema
from django.contrib.auth.decorators import login_required
import copy
from studentApp.models import Student, StudentProfile


def index(request):
    return render(request, 'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def register(request):

    form = SignUpForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('login')
    else:

        form = SignUpForm()

    return render(request, 'registration/register.html', {'form': form})


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return render('dashboard')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html', {})


@login_required
def userLogout(request):
    logout(request)
    return render('login')


@login_required
def admin(request):
    return redirect(admin.site.urls)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def student(request):
    return render(request, 'studentpage.html')

@login_required
def student_profile(request):
    return render(request, 'profilepage.html')

@login_required
def feedback(request):
    return render(request, 'feedbackpage.html')

@login_required
def registerStudent(request):

    if request.method == "GET":
        form = StudentForm()
        return render(request, "registerstudent.html", {'form': form})
    else:
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/dashboard")


@login_required
def profile(request):
    if request.method == "GET":
        form = StudentProfileForm()
        return render(request, 'studentprofile.html', {'form': form})
    else:
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("/dashboard")


@login_required
def get_students(request):
    context = {"getStudents": Student.objects.all()}
    return render(request, "studentsview.html", context)


@login_required
def get_student(request, pk):
    queryset = StudentProfile.objects.get(id=pk)

    context = {
        
        'queryset': queryset
    }

    
    

    return render(request, "student.html", context)


@login_required
def feedback_form(request):

    if request.method == 'POST':

        form = UserFeedbackForm(request.POST)

        if form.is_valid():

            form.save()

            return render(request, 'thanks.html')
    else:

        form = UserFeedbackForm()

    return render(request, 'feedback.html', {'form': form})

# Create your views here.
