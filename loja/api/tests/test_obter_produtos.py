from django.test import TestCase
from django.shortcuts import resolve_url as r


class ProdutoTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('api_name:produtos'))

    def test_get_status(self):
        self.assertEqual(200, self.resp.status_code)