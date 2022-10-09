from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")


def home(request):
    # use django.shortcuts.render to use a html template instead of a string to return as HttpResponse
    # render takes the request argument first and then path to html template after the templates directory onward.
    return render(request, "blog/home.html")


# def about(request):
#     return HttpResponse("<h1>Blog About</h1>")


def about(request):
    return render(request, "blog/about.html")
