from django.urls import path
from . import views

# for home page we use an empty string for path url
urlpatterns = [
    path("", views.home, name="blog-home"),
    path("about/", views.about, name="blog-about"),
]
