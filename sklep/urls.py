from django.urls import path

from .views import (
    product_create_view,
    products_view,
    dynamic_lookup_view,
    product_delete_view,
)

app_name = 'sklep'
urlpatterns = [
    path('', products_view),
    path('create/', product_create_view, name='create_view'),
    path('<int:id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
]
