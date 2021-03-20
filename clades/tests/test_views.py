from django.test import TestCase
from django.urls import reverse_lazy

class CladesViewsTest(TestCase):
    fixtures = ['periparus']

    def visit(self, name, follow=True, **kwargs):
        return self.client.get(reverse_lazy(name), follow=True, **kwargs)

    def test_home(self):
        response = self.visit('clades-home')
        self.assertEqual(200, response.status_code, 'No Home view available')
        
    def test_search(self):
        response = self.visit('clades-search')
        self.assertEqual(200, response.status_code, 'No Search view available')

        response = self.client.post(reverse_lazy('clades-search'),
                                    {'search' :'ater'},
                                    follow=True)

        self.assertIn(b'Coal', response.content, 'Species name not found')

    def test_no_search(self):
        response = self.client.post(reverse_lazy('clades-search'),
                                    {'search' : ''},
                                    follow=True)
        self.assertIn(b'<ul class="errorlist">', response.content,
                      'Invalid form data not detected')
