from django.shortcuts import render
from django.http import HttpResponse

# def index() {
#     return HttpResponse ("главная страница")
# }

def index(request):
    template = "posts/index.html"
    return render(request, template)

def group_posts(): 
    return HttpResponse ("группы")
