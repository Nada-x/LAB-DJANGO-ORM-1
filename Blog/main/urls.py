from django.urls import path,include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    path('mode/dark/', views.dark_view, name="dark_view"),
    path('mode/light/', views.light_view, name="light_view"),
    path("add/", views.add_post, name="add_post"),
    path("all/", views.all_posts, name="all_posts")
]