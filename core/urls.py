"""Users app URL config"""

from django.urls import path
from django.contrib.auth import views as core_views

from . import views

app_name = "core"
urlpatterns = [
    path("home/", views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("stores/", views.StoresView.as_view(), name="stores"),
    path("signup/", views.SignupView.as_view(), name="signup"),

]