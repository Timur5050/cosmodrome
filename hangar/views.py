from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from hangar.forms import (
    UserCreationForm,
    AstronautSearchForm,
    RacketForm,
    FlightForm,
    AstronautCreationForm,
    FlightSearchForm,
    RacketSearchForm, AstronautRegistrationForm
)
from hangar.models import Racket, Astronaut, Flight


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "hangar/index.html")


@login_required
def user_creation_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": AstronautRegistrationForm
        }
        return render(request, "hangar/user_form.html", context=context)

    if request.method == "POST":
        form = AstronautRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse_lazy("hangar:main-page"))
        else:
            context = {
                "form": form
            }
            return render(request, "hangar/user_form.html", context=context)


@login_required
def user_profile_view(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "user": Astronaut.objects.get(id=pk)
    }
    return render(request, "hangar/user_details.html", context=context)


@login_required
def racket_list_view(request: HttpRequest) -> HttpResponse:
    queryset = Racket.objects.all()
    search_name = request.GET.get("name")
    if search_name:
        queryset = queryset.filter(name__icontains=search_name)

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "racket_list": page_obj,
        "search_form": RacketSearchForm,
        "page_obj": page_obj
    }
    return render(request, "hangar/racket_list.html", context=context)


@login_required
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


@login_required
def racket_details(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "racket": Racket.objects.get(id=pk)
    }
    return render(request, "hangar/racket_details.html", context=context)


@login_required
def astronaut_list_view(request: HttpRequest) -> HttpResponse:
    queryset = Astronaut.objects.all()
    search_username = request.GET.get("username")
    if search_username:
        queryset = queryset.filter(username__icontains=search_username)

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "astronaut_list": page_obj,
        "search_form": AstronautSearchForm,
        "page_obj": page_obj
    }
    return render(request, "hangar/astronaut_list.html", context=context)


@login_required
def astronaut_create_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": AstronautCreationForm
        }
        return render(request, "hangar/astronaut_form.html", context=context)

    if request.method == "POST":
        form = AstronautCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("hangar:astronaut-list"))


@login_required
def astronaut_details(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "astronaut": Astronaut.objects.get(id=pk)
    }
    return render(request, "hangar/astronaut_details.html", context=context)


@login_required
def flight_list_view(request: HttpRequest) -> HttpResponse:
    queryset = Flight.objects.all()
    search_name = request.GET.get("name")
    if search_name:
        queryset = queryset.filter(name__icontains=search_name)

    paginator = Paginator(queryset, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "flight_list": page_obj,
        "search_form": FlightSearchForm(),
        "page_obj": page_obj
    }
    return render(request, "hangar/flight_list.html", context=context)


@login_required
def flight_list_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        context = {
            "form": FlightForm
        }
        return render(request, "hangar/flight_form.html", context=context)

    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("hangar:flight-list"))


@login_required
def flight_details(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "flight": Flight.objects.get(id=pk)
    }
    return render(request, "hangar/flight_details.html", context=context)
