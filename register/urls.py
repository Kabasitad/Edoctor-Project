from django.urls import path
from register import views

app_name = "register"

urlpatterns = [

    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

]