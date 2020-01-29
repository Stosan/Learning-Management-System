from django.shortcuts import render,redirect
from .forms import TeacherSignupForm

from Account.models import Account
from Teacher.models import Teacher
from .utils import randomPassword, EmailAuto

from django.contrib.auth.hashers import make_password

from django.contrib import messages

# Create your views here.
def dashboard(request):
    return render(request, 'Manager/dashboard.html')

def teachers_list(request):
    return render(request, 'Manager/Teacher Related/teachers_list.html')

def students_list(request):
    return render(request, 'Manager/Student Related/students_list.html')

def add_teacher_form(request):
    context={
        'AddTeacherForm': TeacherSignupForm,
    }
    if request.method == 'GET':
        return render(request, 'Manager/Teacher Related/add_teacher_form.html', context)
    else:
        email = request.POST.get("email")
        user_name = request.POST.get("username")
        password = randomPassword(10)
        html = f'Please use below autogenerated password to login with your email. Password is </br> <h1> { password} </h1>.'
        user = Account(email = email,username= user_name,  password= make_password(password), is_teacher = True)
        user.save()
        EmailAuto(recipient_list= [email,], html_message = html)
        teacher = Teacher(user = user)
        teacher.save()
        messages.success(request,f"Teacher user '{ user.username }' created successfully.  ")
        return redirect('manager_dashboard')



            
        