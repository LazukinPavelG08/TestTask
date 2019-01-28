from django.urls import path
from . import views
from .get_code import get_code, get_token, get_profiles, get_profile


urlpatterns = [
    path('', views.greeting, name='greeting'),
    path('vk_api', views.vk_api, name='vk_api'),
    path('get_code/', get_code),
    path('get_token/', get_token),
    path('profiles/', get_profiles),
    path('profiles/<int:pk>/', get_profile),
]