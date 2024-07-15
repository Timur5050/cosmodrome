from django.urls import path

from hangar.views import (
    index,
    user_creation_view,
    racket_create_view,
    racket_list_view,
    astronaut_list_view,
    flight_list_view,
    flight_list_create,
    flight_details,
    astronaut_create_view
)

urlpatterns = [
    path("", index, name="main-page"),
    path("registration/", user_creation_view, name="registration"),
    path("rackets/", racket_list_view, name="racket-list"),
    path("rackets/create/", racket_create_view, name="racket-create"),
    path("astronauts/", astronaut_list_view, name="astronaut-list"),
    path("astronauts/create/", astronaut_create_view, name="astronaut-create"),
    path("flights/", flight_list_view, name="flight-list"),
    path("flights/create/", flight_list_create, name="flight-create"),
    path("flights/<int:pk>/details/", flight_details, name="flight-details"),
]

app_name = "hangar"
