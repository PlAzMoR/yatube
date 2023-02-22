from django.shortcuts import render, get_object_or_404
from .models import Post, Group

posts_count = 5

def index(request):
    template = "posts/index.html"
    posts = Post.objects.order_by('-pub_date')[:posts_count]
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    context = {
    'group': group,
    }
    return render(request, template, context)
