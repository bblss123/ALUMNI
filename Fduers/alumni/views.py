from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import User
from .models import Tie
from .models import Tag
from .models import City
from .models import Major
from .models import Department
from .models import Industry


# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user_id')
        password = request.POST.get('user_password')
        user_find = User.objects.filter(username__exact=username, password__exact=password)
        # user = User.objects.filter(username__exact=username, password__exact=password)[:1].get()
        if (user_find):
            user = user_find[0]
            TieList = Tie.objects.all().order_by('-createdTime')
            TieList_OrderbyAccess = Tie.objects.all().order_by('-access')
            TieTOP1 = TieList_OrderbyAccess[:1].get()
            TieTOP2 = TieList_OrderbyAccess[1:2].get()
            TieTOP3 = TieList_OrderbyAccess[2:3].get()
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            return render(request, 'index.html', locals())

        else:
            return render(request, 'fail.html')


def register(request):
    if request.method == 'GET':
        cities = City.objects.all()
        majors = Major.objects.all()
        departments = Department.objects.all()
        industries = Industry.objects.all()
        return render(request, 'register.html', locals())
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
        # major_id = request.POST.get('major_id')
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
            # major_id=major_id
        )
        return render(request, 'success_register.html')


def index(request):
    TieList = Tie.objects.all().order_by('-createdTime')
    TieList_OrderbyAccess = Tie.objects.all().order_by('-access')
    TieTOP1 = TieList_OrderbyAccess[:1].get()
    TieTOP2 = TieList_OrderbyAccess[1:2].get()
    TieTOP3 = TieList_OrderbyAccess[2:3].get()

    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)

    return render(request, 'index.html', locals())


def postTie(request):
    if request.method == 'GET':
        TagList = Tag.objects.all()
        return render(request, 'edit.html', locals())
    else:
        content = request.POST.get('content')
        author_id = request.session.get('user_id')
        title = request.POST.get('title')
        Tie.objects.create(
            title=title,
            author_id=author_id,
            content=content,
            relatedActivity_id=1,
        )
        articles = Tie.objects.all()
        tags = request.POST.getlist('tags')
        print(type(tags))
        print(tags)
        article = articles.order_by('-createdTime')[:1].get()
        article.tag.add(*tags)
        return render(request, 'success_post.html')


def tie(request, tieID):
    tieFind = Tie.objects.get(id=tieID)
    author = tieFind.author
    tieFind.access += 1
    tieFind.save()
    return render(request, 'post.html', locals())