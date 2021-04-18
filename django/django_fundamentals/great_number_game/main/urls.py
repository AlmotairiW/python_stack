from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('check', views.check),
    path('playagain', views.playagain),
    path('leadboard', views.leadboard),
]