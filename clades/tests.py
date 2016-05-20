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
    def test_phylum_name(self):
        phylum = Phylum(name=_PHYLUM_NAME)
        phylum.save()
        self.assertEqual(phylum.name, _PHYLUM_NAME)

    def test_phylum_has_kingdom(self):
        kingdom = Kingdom(name=_KINGDOM_NAME)
        kingdom.save()
        phylum = Phylum(name=_PHYLUM_NAME)
        phylum.kingdom = kingdom
        phylum.save()
        # Retrieve object from DB
        phylum = Phylum.objects.get(name=_PHYLUM_NAME)
        self.assertEqual(phylum.kingdom, kingdom)

