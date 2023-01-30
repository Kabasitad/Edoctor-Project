from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('home1/', views.home1Page, name="home1"),
]
