from django.shortcuts import render
from django.http import HttpResponse

def index(request): #HttpRequest
    return HttpResponse("Страница приложения woman!")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")