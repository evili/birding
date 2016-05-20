from django.test import TestCase

from .models import Kingdom

_KINGDOM_NAME = 'Animalia'

class KingdomTest(TestCase):
    def test_kingdom_name(self):
        kingdom = Kingdom(name=_KINGDOM_NAME)
        kingdom.save()
        self.assertEqual(kingdom.name, _KINGDOM_NAME)
