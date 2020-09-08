from django.urls import path, re_path,include
# views
from .views import (
    ListProductUser,
    ListProductoStock,
    ListProductoGenero
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
    ),
    # ListAPIView
    path(
        'api/producto/por-genero/<str:sexo>/',
        ListProductoGenero.as_view(),
        name='list-pruct-genero'
    )
]