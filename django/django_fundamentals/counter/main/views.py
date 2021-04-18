from django.shortcuts import render, redirect


def index(request):
    if 'visits_counter' in request.session:
        request.session['visits_counter'] += 1
    else:
        request.session['visits_counter'] = 1
    return render(request, "index.html")

def destroy_session(request):
    del request.session['visits_counter']
    del request.session['counter']
    return redirect("/") 

def byTwo(request):
    if 'counter' in request.session:
        request.session['counter'] += 2
        request.session['visits_counter'] += 1
    else:
        request.session['counter'] = 2
        request.session['visits_counter'] += 1
    return render(request, "index.html")

def userCounter(request):
    if 'counter' in request.session:
        count_from_form = request.POST['count']
        request.session['counter'] += int(count_from_form)
        request.session['visits_counter'] += 1
    else:
        count_from_form = request.POST['count']
        request.session['counter'] = int(count_from_form)
        request.session['visits_counter'] += 1
    return render(request, "index.html")
