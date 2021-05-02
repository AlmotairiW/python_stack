from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process_user', views.process_user),
    path('books', views.books),
    path('books/add', views.create_book_review),
    path('create_book', views.create_book),
    path('books/<int:id>', views.get_book),
    path('add_rev/<int:id>', views.add_rev),
    path('delete_rev/<int:bid>/<int:rid>', views.delete_rev),
    path('users/<int:id>', views.user_info),
    path('logout', views.logout),
]