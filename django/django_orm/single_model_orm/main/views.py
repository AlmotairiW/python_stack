from django.shortcuts import render,redirect
from .models import User
# Create your views here.

def index(request):
    context = {
        "all_the_users": User.objects.all()
    }
    return render(request, 'index.html', context)

def process_data(request):

    User.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'],
    email_address = request.POST['email'], age = request.POST['age'] )
    return redirect('/')