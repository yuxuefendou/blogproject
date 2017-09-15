from django.shortcuts import render, get_object_or_404
import markdown
# Create your views here.
from django.http import HttpResponse
from .models import Post

# def index(request):
#     return HttpResponse("欢迎访问我的博客！")
#
#     # return render(request, 'blog/index.html', context={
#     #     'title':'我的博客首页',
#     #     'welcome':'欢迎访问我的首页'
#     # })
#


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    # for post in post_list:
    #     print(post)
    #     print(post.pk)
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })

def detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ]
                                  )
    return render(request, 'blog/detail.html', context={'post': post})



def archives(request,year,month):

    # print(year,month)
    post_list=Post.objects.filter(created_time__year=year,
                                  created_time__month=month).order_by('-created_time')
    # for post in post_list:
    #     print(post.title)

    return render(request,'blog/index.html',context={'post_list':post_list})