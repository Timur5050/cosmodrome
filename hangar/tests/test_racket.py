from django.test import TestCase, Client
from django.urls import reverse

from hangar.forms import RacketSearchForm
from hangar.models import Racket, Astronaut


class RacketTestCase(TestCase):
    def test_racket_str(self):
        racket = Racket.objects.create(
            name="hello",
            speed=900,
            destination="mars"
        )
        self.assertEqual(str(racket), "hello")


class RacketListViewTests(TestCase):
    def setUp(self):
        self.user = Astronaut.objects.create(
            username="test",
            password="test1",
            year_of_experience=10
        )

        self.client = Client()
        self.url = reverse('hangar:racket-list')
        for i in range(15):
            Racket.objects.create(
                name=f'Racket {i + 1}',
                speed=i,
                destination=f"mars{i}"
            )

    def test_racket_list_view_status_code_no_login(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_racket_list_view_status_code_with_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
