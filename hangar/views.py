from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from hangar.forms import UserCreationForm, AstronautCreationForm, RacketForm
from hangar.models import Racket


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "hangar/index.html")


def user_creation_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": AstronautCreationForm
        }
        return render(request, "hangar/user_form.html", context=context)

    if request.method == "POST":
        form = AstronautCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy("hangar:main-page"))
        else:
            context = {
                "form": form
            }
            return render(request, "hangar/user_form.html", context=context)


def racket_view(request: HttpRequest) -> HttpResponse:
    queryset = Racket.objects.all()
    context = {
        "racket_list": queryset
    }
    return render(request, "hangar/racket_list.html", context=context)


def racket_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": RacketForm
        }
        return render(request, "hangar/racket_form.html", context=context)
    if request.method == "POST":
        form = RacketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("hangar:racket-list"))
