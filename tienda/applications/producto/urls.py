from django.urls import path, re_path,include
# views
from .views import (
    ListProductUser
)

app_name= 'product_app'

urlpatterns = [
    path(
        'api/product/por-usuario/',
        ListProductUser.as_view(),
        name='list-by-user'
    )
]