from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def home(request):
#     return HttpResponse("<h1>Blog Home</h1>")

# random dummy data to show how to send dynamic data in html
posts = [
    {
        "author": "Omid Reisi",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "August 28, 2018",
    }
]


def home(request):

    # in order to pass data to our template we create a directory and give the key a random name and set it's value as our data and we can access our data with the set key name.
    context = {
            "posts": posts
            }

    # use django.shortcuts.render to use a html template instead of a string to return as HttpResponse
    # render takes the request argument first and then path to html template after the templates directory onward.
    return render(request, "blog/home.html",context)


# def about(request):
#     return HttpResponse("<h1>Blog About</h1>")


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
