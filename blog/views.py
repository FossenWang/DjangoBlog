from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import CommentForm

import markdown

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def archives(request, year, month):
    post_list = Post.objects.filter(pub_date__startswith=str(year)+'-'+str(month)).order_by('-pub_date')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-pub_date')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.content = markdown.markdown(post.content, 
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)