from django.contrib.auth.forms import UserCreationForm
from django import forms

from hangar.models import Astronaut, Racket


class AstronautCreationForm(UserCreationForm):
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


class RacketForm(forms.ModelForm):
    class Meta:
        model = Racket
        fields = "__all__"
