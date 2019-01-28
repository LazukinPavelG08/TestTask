from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.greeting, name='greeting'),
    url(r'^vk_api', views.vk_api, name='vk_api'),
]