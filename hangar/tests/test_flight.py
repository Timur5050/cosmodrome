from django.test import TestCase
from django.urls import reverse

from hangar.models import Astronaut


class FlightViewTest(TestCase):
    def setUp(self):
        self.astronaut = Astronaut.objects.create(
            username="test",
            password="test1",
            year_of_experience=10
        )

    def test_flight_list_without_login(self):
        response = self.client.get(reverse("hangar:flight-list"))
        self.assertEqual(response.status_code, 302)

    def test_flight_list_with_login(self):
        self.client.force_login(self.astronaut)
        response = self.client.get(reverse("hangar:flight-list"))
        self.assertEqual(response.status_code, 200)
