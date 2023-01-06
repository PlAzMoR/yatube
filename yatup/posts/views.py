from django.shortcuts import render
from django.http import HttpResponse

context = {
    'index': "Это главная страница проекта Yatube",
    'group_posts': "Информация о группах проекта Yatube",
}

def index(request):
    template = "templates/index.html"
    return render(request, template, context)

def group_posts(request):
    template = "templates/group_posts.html" 
    return render(request, template, context)
