"""Users app URL config"""

from django.urls import path
from django.contrib.auth import views as core_views

from . import views

app_name = "users"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="Home"),
    #path("login/", views.LoginView.as_view(), name="login"),
    #path("signup/", views.SignupView.as_view(), name="signup"),
    #path("logout/", core_views.LogoutView.as_view(), name="logout"),
]