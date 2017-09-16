from django.shortcuts import render, get_object_or_404
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView
# Create your views here.
from django.http import HttpResponse
from .models import Post, Category, Tag
from .pagination import pagination


# class IndexView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#     paginate_by = 3

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
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


class IndexView(pagination):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


class ArchiivesView(pagination):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return super(ArchiivesView,self).get_queryset().filter(created_time__year=self.kwargs.get('year'),
                                  created_time__month = self.kwargs.get('month'))
class CategoryView(pagination):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate =get_object_or_404(Category,pk = self.kwargs.get('pk'))
        return  super(CategoryView, self).get_queryset().filter(category = cate)


class TagView(pagination):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView,self).get_queryset().filter(tags=tag)