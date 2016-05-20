from django.test import TestCase

from .models import Kingdom, Phylum

_KINGDOM_NAME = 'Animalia'
_PHYLUM_NAME = 'Chordata'


class CladesTest(TestCase):

    def setUp(self):
        (self.kingdom, created) = Kingdom.objects.get_or_create(
            name=_KINGDOM_NAME)
        (self.phylum, created) = Phylum.objects.get_or_create(
            name=_PHYLUM_NAME,
            kingdom=self.kingdom)


class KingdomTest(CladesTest):
    def test_kingdom_name(self):
        self.assertEqual(self.kingdom.name, _KINGDOM_NAME)

class PhylumTest(CladesTest):
    def test_phylum_name(self):
        self.assertEqual(self.phylum.name, _PHYLUM_NAME)

    def test_phylum_has_kingdom(self):
        phylum = Phylum.objects.get(name=_PHYLUM_NAME)
        self.assertEqual(phylum.kingdom, self.kingdom)
