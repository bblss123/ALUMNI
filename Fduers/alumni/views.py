from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user_id')
        request.session['username'] = username
        password = request.POST.get('user_password')
        user = User.objects.filter(username__exact=username, password__exact=password)
        if (user):
            return redirect('/index')
        else:
            return render(request, 'login.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'username': request.session.get('username')})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        mail = request.POST.get('mail')
        grade = request.POST.get('grade')
        studentID = request.POST.get('studentID')
        phone = request.POST.get('phone')
        referrer = request.POST.get('referrer')
        password = request.POST.get('password')
        city_id = request.POST.get('city_id')
        department_id = request.POST.get('department_id')
        industry_id = request.POST.get('industry_id')
        major_id = request.POST.get('major_id')
        User.objects.create(
            username=username,
            mail=mail,
            grade=grade,
            studentID=studentID,
            phone=phone,
            referrer=referrer,
            password=password,
            city_id=city_id,
            department_id=department_id,
            industry_id=industry_id,
            major_id=major_id
        )
        return render(request, 'success_register.html')
