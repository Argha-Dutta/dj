from django.shortcuts import render

def home(request):
    return render(request, 'student_module/home.html')

def registration(request):
    return render(request, 'student_module/registration.html')

def about_us(request):
    return render(request, 'student_module/about_us.html')
