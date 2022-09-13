from django.urls import path
from . import views

# define the urls
urlpatterns = [
    path('examples', views.example.as_view()),
    path('login', views.login.as_view()),
]