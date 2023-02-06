from django.urls import path
from users import views

app_name = "users"

urlpatterns = [

    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

]