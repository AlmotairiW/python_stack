from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('destroy_session', views.destroy_session),
    path('byTwo', views.byTwo),
    path('userCounter', views.userCounter),
    
]