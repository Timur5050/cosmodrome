from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView, CreateView

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


class UserCreationView(FormView):
    template_name = "hangar/user_form.html"
    form_class = AstronautRegistrationForm
    success_url = reverse_lazy("hangar:main-page")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Astronaut
    template_name = "hangar/user_details.html"
    context_object_name = "user"


class RacketListView(LoginRequiredMixin, ListView):
    model = Racket
    template_name = "hangar/racket_list.html"
    context_object_name = "racket_list"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_name = self.request.GET.get("name")
        if search_name:
            queryset = queryset.filter(name__icontains=search_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = RacketSearchForm()
        return context


class RacketCreateView(LoginRequiredMixin, CreateView):
    model = Racket
    form_class = RacketForm
    template_name = "hangar/racket_form.html"
    success_url = reverse_lazy("hangar:racket-list")


class RacketDetailView(LoginRequiredMixin, DetailView):
    model = Racket
    context_object_name = "racket"
    template_name = "hangar/racket_details.html"


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


class AstronautCreateView(LoginRequiredMixin, CreateView):
    model = Astronaut
    form_class = AstronautCreationForm
    success_url = reverse_lazy("hangar:astronaut-list")
    template_name = "hangar/astronaut_form.html"


class AstronautDetailView(LoginRequiredMixin, DetailView):
    model = Astronaut
    context_object_name = "astronaut"
    template_name = "hangar/astronaut_details.html"


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


class FlightCreateView(LoginRequiredMixin, CreateView):
    model = Flight
    form_class = FlightForm
    template_name = "hangar/flight_form.html"
    success_url = reverse_lazy("hangar:flight-list")


class FlightDetailView(LoginRequiredMixin, DetailView):
    model = Flight
    context_object_name = "flight"
    template_name = "hangar/flight_details.html"
