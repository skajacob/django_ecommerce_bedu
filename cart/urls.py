"""Users app URL config"""

from django.urls import path


from . import views

app_name = "cart"
urlpatterns = [ 
    path("product_list/", views.ProductListView.as_view(), name="product-list"),
    path("product_detail/<slug>", views.ProductDetailView.as_view(), name="product-detail"),
]

