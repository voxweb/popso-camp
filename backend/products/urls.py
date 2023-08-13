from django.urls import path
from products.views import ProductApi

app_name = "products"

urlpatterns = [
    path("", ProductApi.as_view({"get": "list", "post": "create"}), name="stock_list_create"),
]
