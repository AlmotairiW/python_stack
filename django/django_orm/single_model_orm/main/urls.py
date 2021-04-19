from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_data', views.process_data),
]
