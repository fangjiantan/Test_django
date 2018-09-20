# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogArticles

# Create your views here.
def index(request):
    #return HttpResponse("Hello FJT!")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user',username,3600)
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

def event_manage(request):
    username = request.COOKIES.get('user','')
    return render(request,"event_manage.html",{"user":username})

def bolg_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

def blog_article(request,article_id):
    article = BlogArticles.objects.get(id=article_id)
    pub = article.publish
    return render(request,"blog/content.html",{"article":article, "publish":pub })