from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    if 'current_gold' not in request.session:
        request.session['current_gold'] = 0
        request.session['earned'] = 0
    return render(request, 'index.html')

def process_money(request):
    output = ''
    curr_time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    if request.POST['which_loc'] == 'farm':
        earned = int(random.randint(10, 20))
        request.session['current_gold'] += earned
        request.session['earned'] = int(earned)
        output = ('Earned ' + str(earned) + ' golds from the farm! (' 
        + str(curr_time) + ')')
    elif request.POST['which_loc'] == 'cave':
        earned = int(random.randint(5, 10))
        request.session['current_gold'] += earned
        request.session['earned'] = int(earned)
        output = ('Earned ' + str(earned) + ' golds from the cave! (' 
        + str(curr_time) + ')')
    elif request.POST['which_loc'] == 'house':
        earned = int(random.randint(2, 5))
        request.session['current_gold'] += earned
        request.session['earned'] = int(earned)
        output = ('Earned ' + str(earned) + ' golds from the house! (' 
        + str(curr_time) + ')')
    else:
        earned = int(random.randint(-50, 50))
        request.session['current_gold'] += earned
        request.session['earned'] = int(earned)
        if earned < 0:
            output = ('Entered a casino and lost ' + str(earned) + ' golds... Ouch.. (' 
            + str(curr_time) + ')')
        else:
            output = ('Entered a casino and won ' + str(earned) + ' golds! (' 
            + str(curr_time) + ')')

    
    if 'activities' in request.session:
        request.session['activities'].append(output)
    else:
        request.session['activities'] = [output]

    return redirect('/')