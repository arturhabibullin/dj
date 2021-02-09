from django.shortcuts import render
from .models import *
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request,'blog/index.html', context={'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})