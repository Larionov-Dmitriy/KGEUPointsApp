from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *


def register_page(request):
    context = {}
    if request.POST:
        form = StudentCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('profile')
        else:
            context['form'] = form
    else:
        form = StudentCreationForm()
        context['form'] = form
    return render(request, 'Points/register_page.html', context)


def login_page(request):
    context = {}
    if request.POST:
        form = StudentAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('profile')
        else:
            print(form.errors)
    else:
        form = StudentAuthenticationForm()
    context["form"] = form
    return render(request, 'Points/login_page.html', context)


def show_profile(request):
    return render(request, 'Points/profile_page.html')


def logout_user(request):
    logout(request)
    return redirect('login_page')


def update_page(request):
    context = {}
    if request.POST:
        form = StudentUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = StudentUpdateForm(
            initial={
                'email': request.user.email,
                'username': request.user.username,
                'first_name': request.user.first_name,
                'second_name': request.user.second_name,
                'third_name': request.user.third_name,
                'institute': request.user.institute,
                'group': request.user.group,
                'hostel': request.user.hostel,
                'photo': request.user.photo,

            }
        )
    context['form'] = form
    return render(request, 'Points/update_page.html', context)


def rating_page(request):
    students = Student.objects.exclude(username='admin').order_by('-points')
    context = {
        'students': students
    }
    return render(request, 'Points/rating_page.html', context)


def show_points(request):
    student = Student.objects.get(pk=request.user.pk)
    aim = 0
    if student.points:
        aim = int(student.points / 350 * 100)
    context = {
        'student': student,
        'aim': aim
    }
    return render(request, 'Points/points_page.html', context)


def show_details(request):
    details = StudentDetailPoints.objects.filter(student=request.user.pk)
    context = {
        'details': details
    }
    print(details)
    return render(request, 'Points/details_page.html', context)
