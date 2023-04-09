from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Group, User
from django.core.paginator import Paginator
from .utils import get_page_context
from .forms import PostForm

posts_count = 5

# @login_required
def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all()
    context = {
        'page_obj': get_page_context(request, post_list),
    }
    return render(request, template, context)

# @login_required
def group_posts(request, slug):
    template = "posts/group_list.html"
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    context = {
        'group': group,
        'page_obj': get_page_context(request, post_list),
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
    return render(request, template, context)

def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post,
        'post_id': post_id,
    }
    return render(request, template, context)

def post_create(request):
    template = 'posts/create_post.html'
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', request.user)
    context = {'form':form}
    return render(request, template, context)

def post_edit(request, post_id):
    template = 'posts/create_post.html'
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        return redirect('posts:post_detail', post.pk,)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post.save()
        return redirect('posts:post_detail', post.pk,)
    is_edit = True
    context = {
        'form': form,
        'is_edit': is_edit
    }
    return render(request, template, context)
