# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogArticles


import sys;
reload(sys);
sys.setdefaultencoding("utf8")

# Register your models here.
class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")  #作者、发布时间
#    list_filter = ("pubish","anthor")
    search_fields = ('title',"body")  #搜索
#    raw_id_fields = ("author")
#    date_hierarchy = "pubish"
#   ordering = ['pubish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)