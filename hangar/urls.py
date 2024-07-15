from django.urls import path

from hangar.views import (
    index,
    user_creation_view,
    user_profile_view,
    racket_create_view,
    racket_list_view,
    astronaut_list_view,
    flight_list_view,
    flight_list_create,
    flight_details,
    astronaut_create_view,
    racket_details,
    astronaut_details,
)

urlpatterns = [
    path("", index, name="main-page"),
    path("registration/", user_creation_view, name="registration"),
    path("profile/<int:pk>/", user_profile_view, name="user-profile"),
    path("rackets/", racket_list_view, name="racket-list"),
    path("rackets/create/", racket_create_view, name="racket-create"),
    path("rackets/<int:pk>/details/", racket_details, name="racket-details"),
    path("astronauts/", astronaut_list_view, name="astronaut-list"),
    path("astronauts/create/", astronaut_create_view, name="astronaut-create"),
    path("astronauts/<int:pk>/details/", astronaut_details, name="astronaut-details"),
    path("flights/", flight_list_view, name="flight-list"),
    path("flights/create/", flight_list_create, name="flight-create"),
    path("flights/<int:pk>/details/", flight_details, name="flight-details"),
]

app_name = "hangar"
