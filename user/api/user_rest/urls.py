from django.urls import path, include
from .views import api_user_list

urlpatterns= [
  path("users/", api_user_list, name="api_user_list")
]
