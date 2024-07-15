from django.urls import path

from hangar.views import index, user_creation_view, racket_create_view, racket_view


urlpatterns = [
    path("", index, name="main-page"),
    path("registration/", user_creation_view, name="registration"),
    path("rackets/", racket_view, name="racket-list"),
    path("rackets/create/", racket_create_view, name="racket-create"),
]

app_name = "hangar"
