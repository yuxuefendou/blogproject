#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Created on 19:28 2017/9/14 

@author: acer
'''

from django import template
from ..models import Post, Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archivs():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()