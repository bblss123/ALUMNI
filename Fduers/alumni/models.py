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

class Province(models.Model):
    name = models.CharField('省份', max_length=30, null=False, unique=True, primary_key = True)

class City(models.Model):
    name = models.CharField('城市', max_length=30, null=False, unique = False)
    province = models.ForeignKey(Province, on_delete = models.DO_NOTHING, db_column = 'f', default="北京")

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = '城市'

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField('用户名',max_length=30, primary_key = True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='院系')
    mail = models.CharField('邮箱',max_length=20)
    grade = models.IntegerField('届次')
    studentID = models.CharField('学号', max_length=20)
    phone = models.CharField('电话',max_length=20)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING, verbose_name='行业')
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, verbose_name='城市')
    referrer = models.CharField('推荐人',max_length=30,null=True)
    password = models.CharField('密码',max_length=20)
    photo = models.ImageField(upload_to='user_photo/%Y/%m/%d',verbose_name='头像',blank=True, null=True, default='img/default.jpg')
    essay = models.TextField('个性签名', max_length=30, default='')

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
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, verbose_name='所在城市')
    location = models.CharField('详细地点',max_length=200)
    cost = models.PositiveIntegerField('费用')

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = '活动'

    def __str__(self):
        return self.title


class Tie(models.Model):  # means 帖子
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='作者')
    title = models.CharField('标题',max_length=30)
    content = RichTextField()
    createdTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    replyTime = models.DateTimeField(verbose_name='最新回复时间', auto_now=True)
    access = models.IntegerField(default=0, verbose_name='浏览量')
    tag = models.ManyToManyField(Tag, verbose_name='所属标签')
    relatedActivity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, verbose_name='相关活动')

    class Meta:
        verbose_name = '帖子'
        verbose_name_plural = '帖子'

    def __str__(self):
        return self.title


class Reply(models.Model):  # 楼层
    content = models.TextField('回复内容',max_length=200)
    relatedTie = models.ForeignKey(Tie, on_delete=models.DO_NOTHING, verbose_name='相关帖')

    class Meta:
        verbose_name = '楼层'
        verbose_name_plural = '楼层'

class Test(models.Model):
    content = models.TextField(max_length=3000)

    class Meta:
        verbose_name = 'test'
        verbose_name_plural = 'test'

class Student(models.Model): # 存放管理员导入的表单
    name = models.CharField('姓名', max_length = 50)
    studentID = models.CharField('学号', max_length = 20)
    grade = models.IntegerField('界次')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='院系')
