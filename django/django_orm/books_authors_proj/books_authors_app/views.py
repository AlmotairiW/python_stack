from django.shortcuts import render, redirect
from .models import *

# books logic
def books(request):
    context = {
        'all_books': Book.objects.all(),
    }
    return render(request, 'books.html', context)

def add_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/books')

def view_book(request, id):
    if request.method == "POST":
        Book.objects.get( id = id).authors.add(request.POST['selected_author'])

    this_book = Book.objects.get( id = id)
    non_assoc_authors = Author.objects.exclude(books = this_book)
    context = {
        "book_by_id": this_book,
        "non_assoc_authors": non_assoc_authors
    }
    return render(request, 'view_book.html', context)

# Authors logic
def authors(request):
    context = {
        'all_authors': Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def add_author(request):
    Author.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], notes = request.POST['notes'])
    return redirect('/authors')

def view_author(request, id):
    if request.method == "POST":
        Author.objects.get( id = id).books.add(request.POST['selected_book'])

    this_author = Author.objects.get( id = id)
    non_assoc_books = Book.objects.exclude(authors = this_author)
    context = {
        "author_by_id": this_author,
        "non_assoc_books": non_assoc_books,
    }
    return render(request, 'view_author.html', context)