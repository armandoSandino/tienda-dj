from django.urls import path, re_path,include
# views
from .views import (
    ListProductUser,
    ListProductoStock
)

app_name= 'product_app'

urlpatterns = [
    # ListAPIView
    path(
        'api/product/por-usuario/',
        ListProductUser.as_view(),
        name='list-by-user'
    ),
    # ListAPIView
    path(
        'api/product/con-stock/',
        ListProductoStock.as_view(),
        name='list-stock'
    )
]