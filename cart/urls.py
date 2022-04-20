"""Users app URL config"""

from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [ 
    path("cart/", views.ProductListView.as_view(), name="cart"),
]