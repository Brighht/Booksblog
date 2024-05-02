from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login.html", views.login, name="login"),
    path("blogspost.html", views.blogspost, name="blogsposts"),
    path("posts/<str:pk>", views.posts, name="posts")
]