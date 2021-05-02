from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('wall', views.wall),
    path('logout', views.logout),
    path('msg_post', views.msg_post),
    path('msg_comment', views.msg_comment),
    path('del_msg/<int:id>', views.del_msg),
]