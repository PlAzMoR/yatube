from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User
from django.core.paginator import Paginator
from .utils import get_page_context

posts_count = 5

# @login_required
def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all()
    context = {
        'page_obj': get_page_context(request, post_list),
    }
    return render(request, template, context)

@login_required
def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    context = {
    'group': group,
    }
    return render(request, template, context)

def profile(request, username):
    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author=author)
    context = {
        'page_obj': get_page_context(request, post_list),
        'author': author,
    }
    return (request, template, context)

def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'post_id': post_id,
    }
    return (request, template, context)
