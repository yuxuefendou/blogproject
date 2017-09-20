from django.contrib import admin
# Register your models here.
from .models import Post, Category, Tag, Post2
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
# admin.site.register(Post2)

