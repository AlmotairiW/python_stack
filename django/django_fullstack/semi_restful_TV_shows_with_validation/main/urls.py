from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.add_show, name = 'my_add'),
    path('shows/create', views.create, name = 'my_create'),
    path('shows/<int:id>', views.view_show, name = "my_show"),
    path('shows/<int:id>/edit', views.edit_show),
    path("shows/<int:id>/update", views.update),
    path("shows/<int:id>/destroy", views.delete),

    
]