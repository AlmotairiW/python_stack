from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

# Create your views here.


def index(request):
    if 'uid' in request.session:
        context = {
            "this_user": User.objects.get(id=request.session['uid'])
        }
        return render(request, "books.html", context)
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
                name = request.POST['name']
                ali = request.POST['ali']
                email = request.POST['email']
                new_pass = bcrypt.hashpw(
                    request.POST['pass'].encode(), bcrypt.gensalt()).decode()
                new_user = User.objects.create(
                    name = name, alias = ali, email = email, password=new_pass)
                request.session['uid'] = new_user.id
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
                    return redirect('/books')
                else:
                    request.session['is_reg'] = "false"
                    messages.error(request, "invalid Log in")
                    return redirect('/')


def books(request):
    if 'uid' in request.session:
        context = {
            "this_user": User.objects.get(id=request.session['uid']),
            "last_revs": Review.objects.order_by('-id')[:3],
            "all_revs": Review.objects.all(),
        }
        print('last_revs')
        return render(request, "books.html", context)

    else:
        return redirect("/")

def create_book_review(request):
    
    context = {
            "all_authors": Author.objects.all()
        }
    return render(request, "add_book.html", context)

def create_book(request):
    if request.method == 'POST':
        errors = Book.objects.book_validator(request.POST)
        print(len(errors))
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return redirect ('/books/add')
                
        
        title =  request.POST['title']
        added_by = User.objects.get(id = request.session['uid'])
        if(request.POST['c_author']) != "-1":
            print(request.POST['c_author'])
            author = Author.objects.get(id = request.POST['c_author'])
        else:
            author = Author.objects.create(name = request.POST['author'])
            print(request.POST['author'])

        new_book = Book.objects.create(title = title, added_by = added_by, author = author)
        Review.objects.create(review_txt = request.POST['rev'], book = new_book,
        rating = int(request.POST['rat']), user = User.objects.get(id = request.session['uid']))
        return redirect('/books')

def get_book(request, id):
    context = {
        "this_book": Book.objects.get(id = id),
        "this_user": User.objects.get(id = request.session['uid'])
    }
    return render(request, "view_book.html", context)
def add_rev(request, id):
    this_book = Book.objects.get( id = id)
    Review.objects.create(review_txt = request.POST['rev'], book = this_book,
        rating = int(request.POST['rat']), user = User.objects.get(id = request.session['uid']))
    return redirect(f"/books/{id}")

def delete_rev(request, bid, rid):
    rev_to_delete = Review.objects.get(id = rid)
    rev_to_delete.delete()
    return redirect(f"/books/{bid}")

def user_info(request, id):
    context = {
        "this_user": User.objects.get(id = id),
    }
    return render (request,"show_user.html", context)

def logout(request):
    request.session.flush()
    return redirect('/')
