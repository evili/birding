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

    # def test_login(self):
    #     resp = self.visit_view('login')
    #     self.assertEqual(200, resp.status_code, "No login page")

    # def test_logout(self):
    #     resp = self.visit_view('logout')
    #     self.assertEqual(200, resp.status_code, "No logout page")

    # def test_password_change(self):
    #     resp = self.visit_view('password_change')
    #     self.assertEqual(200, resp.status_code, "No password change page")

    # def test_password_change_done(self):
    #     resp = self.visit_view('password_change_done')
    #     self.assertEqual(200, resp.status_code, "No password change done page")

    # def test_password_reset(self):
    #     resp = self.visit_view('password_reset')
    #     self.assertEqual(200, resp.status_code, "No password reset page")
        
    # def test_password_reset_done(self):
    #     resp = self.visit_view('password_reset_done')
    #     self.assertEqual(200, resp.status_code, "No password reset-done page")

    # def test_password_reset_confirm(self):
    #     resp = self.visit_view('password_reset_confirm', kwargs={
    #         'uidb64':'9876543210',
    #         'token': '0123456789-0123456789',
    #     })
    #     self.assertEqual(200, resp.status_code, "No reset-confirm page")

    # def test_password_reset_complete(self):
    #     resp = self.visit_view('password_reset_complete')
    #     self.assertEqual(200, resp.status_code, "No reset-done page")
