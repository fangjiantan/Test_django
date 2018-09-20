# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name="bolg_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)
    def __str__(self):
        return self.title
