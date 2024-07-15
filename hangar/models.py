from django.contrib.auth.models import AbstractUser
from django.db import models


class Racket(models.Model):
    name = models.CharField(max_length=255)
    speed = models.IntegerField()
    destination = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return {self.name}


class Astronaut(AbstractUser):
    year_of_experience = models.IntegerField()

    def __str__(self):
        return self.username


class Flight(models.Model):
    name = models.CharField(max_length=255)
    duration = models.IntegerField()
    astronauts = models.ManyToManyField(Astronaut, related_name="flights")
    racket = models.ForeignKey(Racket, on_delete=models.CASCADE, related_name="flights")
    flight_date = models.DateField()

    def __str__(self):
        return self.name
