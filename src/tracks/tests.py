from django.test import TestCase
from ninja.testing import TestClient

from tracks.api import router

headers = {"Authorization": "Bearer supersecret"}


class HelloTest(TestCase):
    def test_get_tracks(self):
        client = TestClient(router_or_app=router)
        response = client.get("", headers=headers)
        self.assertEqual(response.status_code, 200)
