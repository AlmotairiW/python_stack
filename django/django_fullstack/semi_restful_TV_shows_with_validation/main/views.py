from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return redirect("/shows")


def shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    return render(request, "shows.html", context)


def add_show(request):
    return render(request, "add_show.html")


def create(request):
    if request.method == "POST":
        errors = Show.objects.show_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)

            return render(request, "add_show.html")

        else:
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["rdate"]
            description = request.POST["desc"]
            Show.objects.create(title=title, network=network,
                                release_date=release_date, description=description)
            this_show = Show.objects.last()
    return redirect("my_show", id=this_show.id)


def view_show(request, id):
    context = {
        "this_show": Show.objects.get(id=id)

    }

    return render(request, "view_show.html", context)


def edit_show(request, id):
    context = {
        "this_show": Show.objects.get(id=id)
    }

    return render(request, "edit_show.html", context)


def update(request, id):
    if request.method == "POST":
        errors = Show.objects.show_validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            context = {
                "this_show": Show.objects.get(id=id)
            }

            return render(request, "edit_show.html", context)
        else:
            title = request.POST["title"]
            network = request.POST["network"]
            release_date = request.POST["rdate"]
            description = request.POST["desc"]
            this_show = Show.objects.get(id=id)
            this_show.title = title
            this_show.network = network
            this_show.release_date = release_date
            this_show.description = description
            this_show.save()
    return redirect(f'/shows/{id}')


def delete(request, id):
    this_show = Show.objects.get(id=id)
    this_show.delete()

    return redirect("/shows")
