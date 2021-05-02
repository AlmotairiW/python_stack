from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('books', views.books),
    path('create', views.create_book),
    path('add_fav/<int:id>', views.add_fav),
    path('add_fav2/<int:id>', views.add_fav2),
    path('remove_fav/<int:id>', views.remove_fav),
    path('books/<int:id>', views.view_book),
    path('update/<int:id>', views.update_book),
    path('delete/<int:id>', views.delete_book),
    path('user_fav', views.user_fav),
    path('logout', views.logout),

]