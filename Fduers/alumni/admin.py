from django.contrib import admin
import sys
sys.path.append('../')
from functionality.readexcel import decode
from functionality.importstudentsheet import importdata


# Register your models here.

from .models import *

# class tmp(admin.ModelAdmin):
#     fields = ['name', 'department']

@admin.action(description = '将表单导入后台数据库')
def make_published(modeladmin, request, queryset):
    for item in queryset:
        if item.hasBeenProceeded == True:
            continue
            
        stuList = decode(str(item))
        importdata(Student, Department, stuList)

        item.hasBeenProceeded = True
        item.save()

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['text']}),
        ('正确答案', {'fields': ['rightChoice']}),
    ]
    inlines = [ChoiceInline]

class StudentSheetAdmin(admin.ModelAdmin):
    list_display = ['upload', 'hasBeenProceeded']
    ordering = ['hasBeenProceeded']
    actions = [make_published]

admin.site.register(Tie)
admin.site.register(Activity)
admin.site.register(City)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Department)
admin.site.register(Reply)
admin.site.register(Industry)
admin.site.register(Student)
admin.site.register(StudentSheet, StudentSheetAdmin)
admin.site.register(Question, QuestionAdmin)