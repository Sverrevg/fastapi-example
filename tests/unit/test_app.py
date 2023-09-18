from unittest import TestCase

from tests.test_app import client


class TestApp(TestCase):

    def test_read_root(self) -> None:
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
