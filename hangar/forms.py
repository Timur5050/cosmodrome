from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import DateInput

from hangar.models import Astronaut, Racket, Flight


class AstronautRegistrationForm(UserCreationForm):
    class Meta:
        model = Astronaut
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
            "year_of_experience"
        )
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class AstronautCreationForm(UserCreationForm):
    class Meta:
        model = Astronaut
        fields = UserCreationForm.Meta.fields + (
            "year_of_experience",
        )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class RacketForm(forms.ModelForm):
    class Meta:
        model = Racket
        fields = "__all__"


class FlightForm(forms.ModelForm):
    astronauts = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    flight_date = forms.DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Flight
        fields = "__all__"


class FlightSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="",
        max_length=255,
        widget=forms.TextInput(attrs={"placeholder": "search by name"}),
    )


class RacketSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        label="",
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "search by name"})
    )


class AstronautSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "search by username"})
    )
