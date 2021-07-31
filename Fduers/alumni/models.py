from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Department(models.Model):
    name = models.CharField('院系', max_length=30, null=False, unique=True)

    class Meta:
        verbose_name = '院系'
        verbose_name_plural = '院系'

    def __str__(self):
        # 作用：外键约束中指定关联到哪一个属性上去，譬如这里关联到self.name
        return self.name


class Industry(models.Model):
    name = models.CharField('行业', max_length=30, null=False, unique=True)

    class Meta:
        verbose_name = '行业'
        verbose_name_plural = '行业'

    def __str__(self):
        return self.name

class ProvinceID(models.Model):
    name = models.CharField('省份', max_length=30, null=False, unique=True)

class Province(models.Model):
    # id = models.IntegerField(primary_key = True)
    name = models.CharField('省份', max_length=30, null=False, unique=True, primary_key = True)

class City(models.Model):
    name = models.CharField('城市', max_length=30, null=False, unique = False)
    province = models.ForeignKey(Province, on_delete = models.CASCADE, db_column = 'f', default="北京")

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'

    def __str__(self):
        return self.name

class Student(models.Model): # 存放管理员导入的表单
    name = models.CharField('姓名', max_length = 50)
    studentID = models.CharField('学号', max_length = 20, unique = True)
    grade = models.IntegerField('界次')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='院系')
    used = models.BooleanField('是否已被注册', default=False)

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
    
    def __str__(self):
        return self.studentID + ' ' + self.name

class User(models.Model):
    username = models.CharField('用户名',max_length=30, primary_key = True)
    gender = models.CharField('性别', default='hidden', max_length=20)
    mail = models.EmailField('邮箱',max_length=200)
    phone = models.CharField('电话',max_length=20)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, verbose_name='行业')
    # city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='城市')

    prov_id = models.IntegerField('地域')

    referrer = models.CharField('推荐人',max_length=30,null=True)
    password = models.CharField('密码',max_length=20)
    photo = models.ImageField(upload_to='user_photo/%Y/%m/%d',verbose_name='头像',blank=True, null=True, default='static/img/default.jpg')
    essay = models.TextField('个性签名', max_length=30, default='')

    stu = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='关联学生')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
#
# class Group(models.Model):
#     groupname = models.CharField('群组名',max_length=10)
#     intr = models.TextField('简介', max_length=200)
#     menbers = models.ManyToManyField(to='User')
#     createdTime = models.DateTimeField('创建时间', auto_now_add=True)

# ####################################################################################################

class Tag(models.Model):

    name = models.CharField('标签', max_length=30, null=False, unique=True)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

    def __str__(self):
        return self.name


class Activity(models.Model):
    title = models.CharField('标题', max_length=30, default='DEFAULT')
    startTime = models.DateTimeField(verbose_name='开始时间')
    endTime = models.DateTimeField(verbose_name='结束时间')
    # city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='所在城市')
    location = models.CharField('详细地点',max_length=200)
    cost = models.PositiveIntegerField('费用')

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = '活动'

    def __str__(self):
        return self.title


class Tie(models.Model):  # means 帖子
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    title = models.CharField('标题',max_length=30)
    content = RichTextField()
    createdTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    replyTime = models.DateTimeField(verbose_name='最新回复时间', auto_now=True)
    access = models.IntegerField(default=0, verbose_name='浏览量')
    # tag = models.ManyToManyField(Tag, verbose_name='所属标签')
    relatedActivity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name='相关活动')

    provID = models.IntegerField('地域', default = 0)
    indusID = models.IntegerField('行业', default = 0)

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return self.title


class Reply(models.Model):  # 楼层
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField('回复内容',max_length=200)
    relatedTie = models.ForeignKey(Tie, on_delete=models.CASCADE, verbose_name='相关帖')
    createdTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    replyThumbNum = models.IntegerField(default = 0)

    class Meta:
        verbose_name = '楼层'
        verbose_name_plural = '楼层'

class Test(models.Model):
    content = models.TextField(max_length=3000)

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'test'

class StudentSheet(models.Model): # 存放管理员上传的同学表单
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    hasBeenProceeded = models.BooleanField(default = False)
    
    class Meta:
        verbose_name = '学生表单'
        verbose_name_plural = '学生表单'
    
    def __str__(self):
        return str(self.upload)

class Question(models.Model):

    class Answer(models.IntegerChoices):
        A = 1
        B = 2
        C = 3

    text = models.CharField('问题描述', max_length = 200)
    rightChoice = models.IntegerField('正确选项', default = 1, choices = Answer.choices)

    class Meta:
        verbose_name = '注册问题'
        verbose_name_plural = '注册问题'
    
    def __str__(self):
        return self.text

class Choice(models.Model):
    text = models.CharField('选项描述', max_length = 200)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)

    def __str__(self):
        return self.text

class User_Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete = models.CASCADE)

class Stars(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    activity = models.ForeignKey(Tie, on_delete = models.CASCADE)
