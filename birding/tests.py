import unittest
from django.test import Client
from django.urls import reverse
    
class BasicUrlsTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def visit_view(self, name, follow=True, kwargs=None):
        return self.client.get(reverse(name, kwargs=kwargs), follow=follow)

    def test_health(self):
        resp = self.visit_view('health')
        self.assertEqual(200, resp.status_code, "No health page")

    def test_login(self):
        resp = self.visit_view('login')
        self.assertEqual(200, resp.status_code, "No login page")
