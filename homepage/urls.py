from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    ]


