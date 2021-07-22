from django.db import migrations, models
import django.db.models.deletion
import django.apps
import sqlite3
import sys
sys.path.append('../')
from alumni.models import *

def importdata(Student, Department, stuList):
    # Student = apps.get_model('alumni', 'Student')
    # Department = apps.get_model('alumni', 'Department')

    for row in stuList:
        if Student.objects.filter(studentID = row[1]).exists() == False:
            tmp = Student(name = row[0], studentID = row[1], department = Department.objects.filter(name = row[2])[0], grade = row[3])
            print(row[0], row[1], row[2], row[3])
            tmp.save()