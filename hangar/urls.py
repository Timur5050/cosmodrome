from django.urls import path

from hangar.views import index


urlpatterns = [
    path("", index, name="main-page")
]

app_name = "hangar"
