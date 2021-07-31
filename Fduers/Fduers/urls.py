"""Fduers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from alumni import views
from Fduers import settings
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('', views.login),
    path('index/', views.index),
    path('register/', views.register),
    path('postTie/', views.postTie),
    re_path(r'tie/(?P<tieID>\d+)/$', views.tie),
    path('submit/',views.submit),
    path('score/', views.score),
    path('about/', views.about),
    path('tieLists/', views.tieLists),
    path('postTie/', views.postTie),
    path('messageBoard/', views.messageBoard),
    path('activities/', views.activities),
    re_path(r'tieLists/province/(?P<provID>\d+)', views.tieListsProv),
    re_path(r'tieLists/industry/(?P<indusID>\d+)', views.tieListsIndus),
    path('changemessage/', views.changemessage),
    path('tieLists/stars/', views.tieListsStars),
    path('stars/', views.stars),
    path('myactivities/', views.myactivities),
    path('logout/', views.logout),
    path('mypost/', views.mypost),
    path('myreply/', views.myreply)
]

