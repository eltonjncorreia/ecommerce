from django.test import TestCase
from django.shortcuts import resolve_url as r


class PeditoApiTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('api:pedidos'))

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)
