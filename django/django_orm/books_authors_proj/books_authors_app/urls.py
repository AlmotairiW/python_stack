from django.urls import path
from . import views

urlpatterns = [
    path('', views.books),
    path('add_book', views.add_book),
    path('books/<int:id>', views.view_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('authors/<int:id>', views.view_author),

]
