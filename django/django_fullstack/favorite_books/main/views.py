from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.


def index(request):
    if 'uid' in request.session:

        return redirect('/books')

    else:
        return render(request, "login_reg.html")


def process_user(request):
    if request.method == 'POST':
        is_reg = request.POST.get('type')
        if is_reg == 'reg':  # registration
            errors = User.objects.reg_validator(request.POST)
            if len(errors) > 0:
                for key, val in errors.items():
                    messages.error(request, val)
                request.session['is_reg'] = "true"
                return redirect('/')
            else:
                fname = request.POST['fname']
                lname = request.POST['lname']
                email = request.POST['email']
                new_pass = bcrypt.hashpw(
                    request.POST['pass'].encode(), bcrypt.gensalt()).decode()
                new_user = User.objects.create(
                    first_name=fname, last_name=lname, email=email, password=new_pass)
                request.session['uid'] = new_user.id
                request.session['is_reg'] = "true"
                return redirect('/books')
        else:  # log in
            errors = User.objects.login_validator(request.POST)
            if len(errors) > 0:
                for key, val in errors.items():
                    messages.error(request, val)
                request.session['is_reg'] = "false"
                return redirect('/')
            else:
                # made sure email is unique upon registration
                logged_user = User.objects.get(email=request.POST['email'])
                if bcrypt.checkpw(request.POST['pass'].encode(), logged_user.password.encode()):
                    request.session['uid'] = logged_user.id
                    request.session['is_reg'] = "false"
                    return redirect('/books')
                else:
                    messages.error(request, "invalid Log in")
                    return redirect('/')


def books(request):
    if 'uid' in request.session:
        context = {
            "this_user": User.objects.get(id=request.session['uid']),
            "all_books" : Book.objects.all(),
        }
        return render(request, "books.html", context)
    return redirect('/')


def create_book(request):
    if request.method == 'POST':
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return redirect('/books')
        else:
            title = request.POST['title']
            desc = request.POST['desc']
            up_by = User.objects.get(id = request.session['uid'])
            added_book = Book.objects.create(title = title, desc = desc, 
            uploaded_by = up_by)
            added_book.users_who_like.add(up_by)

            return redirect('/books') 

def add_fav(request, id):
    this_book = Book.objects.get(id = id)
    this_book.users_who_like.add(User.objects.get(id = request.session['uid']))
    return redirect('/books')

def add_fav2(request, id):
    this_book = Book.objects.get(id = id)
    this_book.users_who_like.add(User.objects.get(id = request.session['uid']))
    return redirect(f'/books/{id}')

def remove_fav(request, id):
    this_book = Book.objects.get(id = id)
    this_book.users_who_like.remove(User.objects.get(id = request.session['uid']))
    return redirect(f"/books/{id}")

def view_book(request, id):
    context = {
        "this_user": User.objects.get(id = request.session['uid']),
        "this_book" : Book.objects.get(id = id),
        }
    return render(request, "view_book.html", context)

def update_book(request, id):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect(f'/books/{id}')
    else:
        book_to_update = Book.objects.get(id = id)
        book_to_update.title = request.POST['title']
        book_to_update.desc = request.POST['desc']
        book_to_update.save()
        return redirect("/books")
    
def delete_book(request, id):
    Book.objects.get(id = id).delete()
    return redirect("/books")

def user_fav(request):
    context = {
        "this_user": User.objects.get(id = request.session['uid']),
        }
    return render(request, "user_favs.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
