from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'all_dojos' : Dojo.objects.all()
    }
    return render(request, "index.html", context)

def process_dojo(request):
    Dojo.objects.create(name = request.POST['name'], city =  request.POST['city'],
    state = request.POST['state'], desc = " new dojo")

    return redirect('/')

def process_ninja(request):
    ninja_dojo = Dojo.objects.get(id = request.POST['loc'])
    Ninja.objects.create(first_name = request.POST['fname'], last_name = request.POST['lname'], dojo = ninja_dojo)
    return redirect('/')