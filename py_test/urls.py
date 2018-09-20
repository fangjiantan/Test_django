from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.bolg_title,name="bolg_title"),
    url(r'(?P<article_id>\d)/$',views.blog_article,name="blog_detail"),
]