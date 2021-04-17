from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def result(request):
    name_from_form = request.POST['name']
    locatiom_from_form = request.POST['location']
    fav_lang_from_form = request.POST['favLang']
    comnts_from_form = request.POST['comments']
    gender_from_form = request.POST['gender']
    stacks_from_form = request.POST.getlist('checks []')
    context = {
        "name_on_template" : name_from_form,
        "location_on_template" : locatiom_from_form,
        "fav_lang_on_template" : fav_lang_from_form,
        "comnts_on_templates": comnts_from_form,
        "gender_on_tempalte" : gender_from_form,
        "stack_on_template" : stacks_from_form

    }
    return render (request, 'results.html', context)

