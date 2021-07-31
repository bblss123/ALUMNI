import json
import os

from django.shortcuts import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import *
from django.core.files.base import ContentFile
from django.utils import timezone

from django.core.files import File
from io import BytesIO



# Create your views here.

def about(request):
    return render(request, 'about.html')


def login(request):
    if request.session.get('username') != None:
        return HttpResponseRedirect('/index/')
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user_id')
        password = request.POST.get('user_password')
        user_find = User.objects.filter(username__exact=username, password__exact=password)
        # user = User.objects.filter(username__exact=username, password__exact=password)[:1].get()
        if (user_find):
            # return render(request, 'success.html')
            user = user_find[0]
            # request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['stuid'] = user.stu_id
            return HttpResponseRedirect('/index/')
        else:
            return render(request, 'fail_login.html')


# 验证学生信息
def submit(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        return render(request, 'submit.html', locals())
    else:
        name = request.POST.get('name')
        grade = request.POST.get('grade')
        department_id = request.POST.get('department_id')
        studentID = request.POST.get('studentID')
        student_find = Student.objects.filter(name__exact=name, grade__exact=grade, studentID__exact=studentID,
                                              department_id__exact=department_id)
        if (student_find):
            student = student_find[0]
            if (student.used == True):
                return render(request, 'fail_reg1.html')
            else:
                request.session['stuID'] = student.id
                return redirect('/score')
        else:
            return render(request, 'fail_reg2.html')


# 问答匹配
def score(request):
    if request.method == 'GET':
        questionList = Question.objects.all()
        choiceList = []
        for qt in questionList:
            choiceList.append(Choice.objects.filter(question=qt))
        # print(choiceList)
        return render(request, 'questionary.html', locals())
    if request.method == 'POST':
        questions = Question.objects.all()

        flag = True
        it = 1
        for qt in questions:
            answer = qt.rightChoice
            flag = flag and (answer == int(request.POST['q' + str(it)]))
            it = it + 1

        if flag:
            return redirect('/register')
        else:
            return render(request, 'fail_reg3.html')


def register(request):
    if request.method == 'GET':
        usernames = list(User.objects.values_list('username', flat=True))

        # cities = City.objects.all()
        provinces = ProvinceID.objects.all()
        industries = Industry.objects.all()

        return render(request, 'register.html', locals())
    else:
        username = request.POST.get('username')
        gender = request.POST['gender']
        mail = request.POST.get('mail')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        prov_id = request.POST.get('city_id')  # city_id represents prov_id
        industry_id = request.POST.get('industry_id')
        essay = request.POST.get('essay')
        # print(request.session)
        stu_id = request.session.get('stuID')
        User.objects.create(
            username=username,
            gender=gender,
            mail=mail,
            phone=phone,
            password=password,
            essay=essay,
            prov_id=prov_id,
            industry_id=industry_id,
            stu_id=stu_id,
        )
        student = Student.objects.get(id=stu_id)
        student.used = True
        student.save()
        return render(request, 'success_register.html')


def index(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    TieList = Tie.objects.all().order_by('-createdTime')
    TieList_OrderbyAccess = Tie.objects.all().order_by('-access')
    department = user.stu.department

    img_pth = user.photo

    # ------------------------------ actcnt

    actcnt = 0

    activityLists = User_Activity.objects.filter(user_id = username)

    for item in activityLists:
        activityID = item.activity_id
        if activityID == 1:
            continue
        print(activityID)
        act = Activity.objects.get(id = activityID)
        provID = Tie.objects.get(relatedActivity_id = activityID).provID
        print('provID = ', provID)
        prov = ProvinceID.objects.get(id = provID).name

        if act.endTime < timezone.now():
            pass
        else:
            actcnt = actcnt + 1

    # -------------------------------------------

    msgcnt = 0

    myTieList = Tie.objects.filter(author_id = username)
    mytiecnt = 0
    for item in myTieList:
        mytiecnt = mytiecnt + 1

    replyList = Reply.objects.filter(user_id = username)
    replycnt = 0
    for item in replyList:
        replycnt = replycnt + 1

    province = ProvinceID.objects.all()

    myprov = user.prov_id

    cnt = 0
    HotList = TieList_OrderbyAccess
    # for tie in TieList_OrderbyAccess:
    #     cnt = cnt + 1
    #     HotList.append(tie)
    #     if cnt == 5:
    #         break

    industry = Industry.objects.all().order_by('-id')

    return render(request, 'home1.html', locals())


def postTie(request):
    if request.method == 'GET':
        # TagList = Tag.objects.all()
        industry = Industry.objects.all()
        province = ProvinceID.objects.all()
        username = request.session.get('username')
        user = User.objects.get(username=username)
        return render(request, 'posttie.html', locals())
    else:
        content = request.POST.get('content')
        username = request.session.get('username')
        title = request.POST.get('title')
        prov = request.POST.get('tagProv')
        indus = request.POST.get('tagJob')

        provID = 0
        if ProvinceID.objects.filter(name = prov).exists():
            provID = ProvinceID.objects.get(name = prov).id
        
        indusID = 0
        if Industry.objects.filter(name = indus).exists():
            indusID = Industry.objects.get(name = indus).id

        isActivity = request.POST.get('isActivity')
        
        relatedActivity_id = 1
        if isActivity == 'True':
            startTime = request.POST.get('starttime')
            endTime = request.POST.get('endtime')
            location = request.POST.get('actplace')
            cost = request.POST.get('cost')

            newAct = Activity.objects.create(
                title = title,
                startTime = startTime,
                endTime = endTime,
                location = location,
                cost = cost
            )
            relatedActivity_id = newAct.id

            User_Activity.objects.create(
                user_id = username,
                activity_id = relatedActivity_id
            )


        Tie.objects.create(
            title=title,
            author_id=username,
            content=content,
            relatedActivity_id = relatedActivity_id,
            indusID = indusID,
            provID = provID
        )

        # articles = Tie.objects.all()
        
        # article = articles.order_by('-createdTime')[:1].get()
        # article.tag.add(*tags)
        return render(request, 'success_post.html')


def tie(request, tieID):
    industry = Industry.objects.all()
    province = ProvinceID.objects.all()
    username = request.session.get('username')
    user = User.objects.get(username=username)
    tieFind = Tie.objects.get(id=tieID)
    author = tieFind.author

    _reply = Reply.objects.filter(relatedTie_id=tieID)

    reply = _reply.order_by('-createdTime')

    # flag = tieFind.relatedActivity_id == 1 ? False : True

    flag = False
    if tieFind.relatedActivity_id != 1:
        flag = True

    if request.method == 'GET':
        tieFind.access += 1
        tieFind.save()
        return render(request, 'tie(4).html', locals())
    elif request.method == 'POST':
        content = request.POST.get('content')
        # if content == NULL:
        author_id = request.session.get('username')
        Reply.objects.create(
            user_id = username,
            content=content,
            relatedTie_id=tieID
        )
        return render(request, 'success_post.html', locals())


def tieLists(request):
    HotList = Tie.objects.all()
    return render(request, 'TieLists.html')


# def postTie(request):
#     if request.method == 'GET':
#         industry = Industry.objects.all()
#         province = Province.objects.all()
#         username = request.session.get('username')
#         user = User.objects.get(username=username)
#         return render(request, 'posttie.html', locals())
#     else if request.method == 'POST':
#         return redirect

def messageBoard(request):
    industry = Industry.objects.all()
    province = ProvinceID.objects.all()
    username = request.session.get('username')
    user = User.objects.get(username=username)
    return render(request, 'message_board.html', locals())


def activities(request):
    industry = Industry.objects.all()
    province = ProvinceID.objects.all()
    username = request.session.get('username')
    user = User.objects.get(username=username)

    activityLists = Activity.objects.all()

    activityList_undone = []
    activityList_done = []
    for act in activityLists:
        activityID = act.id
        if activityID == 1:
            continue
        print('???', activityID)
        provID = Tie.objects.get(relatedActivity_id = activityID).provID
        print('provID = ', provID)
        prov = ProvinceID.objects.get(id = provID).name

        if act.endTime < timezone.now():
            activityList_done.append([act.title, prov, act.endTime])
        else:
            activityList_undone.append([act.title, prov, act.endTime])


    return render(request, 'activities.html', locals())

def myactivities(request):
    industry = Industry.objects.all()
    province = ProvinceID.objects.all()
    username = request.session.get('username')
    user = User.objects.get(username=username)

    activityLists = User_Activity.objects.filter(user_id = username)

    activityList_undone = []
    activityList_done = []
    for item in activityLists:
        activityID = item.activity_id
        if activityID == 1:
            continue
        print(activityID)
        act = Activity.objects.get(id = activityID)
        provID = Tie.objects.get(relatedActivity_id = activityID).provID
        print('provID = ', provID)
        prov = ProvinceID.objects.get(id = provID).name

        if act.endTime < timezone.now():
            activityList_done.append([act.title, prov, act.endTime])
        else:
            activityList_undone.append([act.title, prov, act.endTime])


    return render(request, 'activities.html', locals())


def tieListsProv(request, provID):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')

    prov = ProvinceID.objects.get(id=provID)
    name = prov.name

    print(provID)
    HotList = Tie.objects.filter(provID=provID)

    for item in HotList:
        print(item.title)
    return render(request, 'TieLists.html', locals())


def tieListsIndus(request, indusID):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')

    indus = Industry.objects.get(id=indusID)
    name = indus.name

    HotList = Tie.objects.filter(indusID=indusID)
    for item in HotList:
        print(item.title)
    
    return render(request, 'TieLists.html', locals())


def changemessage(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')
    if request.method == 'GET':
        user_stuid = request.session.get('stuid')
        user = User.objects.get(stu_id=user_stuid)
        provinces = ProvinceID.objects.all()
        industries = Industry.objects.all()
        return render(request, 'rewriteInformation(2).html', locals())
    else:
        user_stuid = request.session.get('stuid')
        user = User.objects.get(stu_id=user_stuid)
        # file_content = ContentFile(request.FILES['uploadphoto'].read())
        file = request.FILES.get('photo')

        print(type(file))



        # assert(False)

        user.photo.save(request.FILES['photo'].name, File(file))

        password = request.POST.get('password')
        prov_id = request.POST.get('city_id')  # city_id represents prov_id
        industry_id = request.POST.get('industry_id')
        # user.username = username
   
        user.password = password
        user.prov_id = prov_id
        user.industry_id = industry_id
        user.save()

        # assert(False)
        # user.save()
        return render(request, 'success.html')


def tieListsStars(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')

    name = '我关注的帖子'

    HotList = Stars.objects.filter(user_id=username)
    # for item in HotList:
    #     print(item.title)
    
    return render(request, 'TieLists.html', locals())

def stars(reque):
    return HttpResponse(ret)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def mypost(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')

    name = '我的发帖'
    HotList = Tie.objects.filter(author_id=username)

    return render(request, 'TieLists.html', locals())

def myreply(request):
    username = request.session.get('username')
    user = User.objects.get(username=username)
    province = ProvinceID.objects.all()
    industry = Industry.objects.all().order_by('-id')

    name = '我的回复'
    ReplyList = Reply.objects.filter(user_id = username)
    HotList = []
    for item in ReplyList:
        # tie = Tie.objects.filter(id = item.)
        HotList.append(item.relatedTie)
    
    return render(request, 'TieLists.html', locals())
