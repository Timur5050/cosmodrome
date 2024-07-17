from django.test import TestCase, Client
from django.urls import reverse

from hangar.forms import RacketSearchForm
from hangar.models import Racket, Astronaut


class AstronautTestCase(TestCase):
    def setUp(self):
        self.astronaut = Astronaut.objects.create(
            username="test",
            password="test1",
            year_of_experience=10
        )

    def test_racket_str(self):
        self.assertEqual(str(self.astronaut), "test")

    def test_astronaut_list_view(self):
        self.client.force_login(self.astronaut)
        response = self.client.get(reverse('hangar:astronaut-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hangar/astronaut_list.html')

    def test_astronaut_create_view(self):
        self.client.force_login(self.astronaut)
        response = self.client.get(reverse('hangar:astronaut-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'hangar/astronaut_form.html')
