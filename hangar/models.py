from django.contrib.auth.models import AbstractUser
from django.db import models


class Racket(models.Model):
    name = models.CharField(max_length=255)
    speed = models.IntegerField()
    destination = models.CharField(max_length=255)


class Astronaut(AbstractUser):
    year_of_experience = models.IntegerField()


class Flight(models.Model):
    duration = models.IntegerField()
    astronauts = models.ManyToManyField(Astronaut, related_name="flights")
    racket = models.ForeignKey(Racket, on_delete=models.CASCADE, related_name="flights")
