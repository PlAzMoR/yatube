from django.shortcuts import render
from django.http import HttpResponse

# context = {
#     'index': "Это главная страница проекта Yatube",
#     'group_posts': "Информация о группах проекта Yatube",
# }

def index(request):
    template = "posts/index.html"
    context = {
    'index': "Это главная страница проекта Yatube",
    }
    return render(request, template, context)

def group_posts(request):
    template = "posts/group_list.html"
    context = {
    'group_list': "Информация о группах проекта Yatube",
    }
    return render(request, template, context)
