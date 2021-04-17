from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('results', views.result),
    path('index', views.index),
]