from django.test import TestCase

from .models import Kingdom, Phylum

_KINGDOM_NAME = 'Animalia'
_PHYLUM_NAME = 'Chordata'

class KingdomTest(TestCase):
    def test_kingdom_name(self):
        kingdom = Kingdom(name=_KINGDOM_NAME)
        kingdom.save()
        self.assertEqual(kingdom.name, _KINGDOM_NAME)

class PhylumTest(TestCase):

    def setUp(self):
        self.kingdom = Kingdom(name=_KINGDOM_NAME)
        self.kingdom.save()

    def test_phylum_name(self):
        phylum = Phylum(name=_PHYLUM_NAME, kingdom=self.kingdom)
        phylum.save()
        self.assertEqual(phylum.name, _PHYLUM_NAME)

    def test_phylum_has_kingdom(self):
        phylum = Phylum(name=_PHYLUM_NAME, kingdom=self.kingdom)
        phylum.save()
        # Retrieve object from DB
        phylum = Phylum.objects.get(name=_PHYLUM_NAME)
        self.assertEqual(phylum.kingdom, self.kingdom)

