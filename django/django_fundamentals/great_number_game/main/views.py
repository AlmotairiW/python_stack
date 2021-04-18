from django.shortcuts import render, redirect
from django.template.defaulttags import register
import random

def index(request):
    if 'number' in  request.session:
        return render(request, 'index.html')
    else:
        request.session['number'] = int(random.randint(1, 100))
        request.session['user_guess'] = -1
        return render(request, 'index.html')


def check(request):
    request.session['user_guess'] = int(request.POST['guess'])
    if 'attempts' in  request.session:
        request.session['attempts'] += 1
    else:
        request.session['attempts'] = 1

    if int(request.POST['guess'])  > request.session['number']:
        request.session['hint'] = 'Too hight!'
        request.session['color'] = 'red'
    elif int(request.POST['guess'])  < request.session['number']:
        request.session['hint'] = 'Too low!'
        request.session['color'] = 'red'
    else:
        request.session['hint'] = 'correct'
        request.session['color'] = 'green'
    return redirect('/')

def playagain(request):
    del request.session['number']
    del request.session['user_guess']
    del request.session['hint']
    del request.session['color']
    del request.session['attempts']
    return redirect('/')

def leadboard(request):
    if "winners" in request.session:
        request.session['winners'].append(request.POST['name'])
        request.session.save()
        request.session['user_attempts'].append(request.session['attempts'])
        request.session.save()
    else:
        request.session['winners'] = [request.POST['name']]
        request.session['user_attempts'] = [request.session['attempts']]
    
    return render(request, 'leadboard.html')

    



