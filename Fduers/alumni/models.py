from django.db import models


# Create your models here.

class Department(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Major(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Industry(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    major = models.ForeignKey(Major, on_delete=models.DO_NOTHING)
    mail = models.CharField(max_length=20)
    grade = models.IntegerField()
    studentID = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    industry = models.ForeignKey(Industry, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    referrer = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


# ####################################################################################################

class Tag(models.Model):
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Activity(models.Model):
    id = models.IntegerField(primary_key=True)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=200)
    cost = models.PositiveIntegerField()


class Tie(models.Model):  # means 帖子
    id = models.IntegerField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='username')
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=200)
    createdTime = models.DateTimeField()
    replyTime = models.DateTimeField()
    access = models.IntegerField(default=0)
    tag = models.ForeignKey(Tag, on_delete=models.DO_NOTHING)
    relatedActivity = models.ForeignKey(Activity, on_delete=models.DO_NOTHING)


class Reply(models.Model):  # 楼层
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    relatedTie = models.ForeignKey(Tie, on_delete=models.DO_NOTHING)
