from django.shortcuts import render, get_object_or_404
import markdown
from comments.forms import CommentForm
# Create your views here.
from django.http import HttpResponse
from .models import Post, Category

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

# def detail(request,pk):
#     post=get_object_or_404(Post, pk=pk)
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                      'markdown.extensions.extra',
#                                      'markdown.extensions.codehilite',
#                                      'markdown.extensions.toc',
#                                   ]
#                                   )
#     form = CommentForm()
#     comment_list = post.comment_set.all()
#     context = {
#         'post':post,
#         'form':form,
#         'comment_list':comment_list
#     }
#     return render(request, 'blog/detail.html', context=context)
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)


def archives(request,year,month):

    # print(year,month)
    post_list = Post.objects.filter(created_time__year=year,
                                  created_time__month=month).order_by('-created_time')
    # for post in post_list:
    #     print(post.title)

    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(  category= cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list':post_list})
