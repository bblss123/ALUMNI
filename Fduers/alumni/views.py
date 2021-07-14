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
        if(user):
            return redirect('/index')
        else:
            return render(request, 'login.html')


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {'username':request.session.get('username')})


def search(request):
    if request.method == 'GET':
        return render(request, 'home.html', {'title': request.session.get('username')})
    else:
        # process
        return render(request, 'home.html', {'title': 'hi'})
        # return redirect('/')


def post(request):
    if request.method == 'POST':
        return render(request, 'https://www.baidu.com')
