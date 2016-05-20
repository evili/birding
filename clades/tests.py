from django.test import TestCase

from .models import Kingdom, Phylum

_KINGDOM_NAME = u'Animalia'
_PHYLUM_NAME = u'Chordata'


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
    def test_kingdom_as_string(self):
        self.assertEqual(str(self.kingdom), _KINGDOM_NAME)
        self.assertEqual(u'%s' % self.kingdom, _KINGDOM_NAME)

class PhylumTest(CladesTest):

    def test_phylum_has_kingdom(self):
        phylum = Phylum.objects.get(name=_PHYLUM_NAME)
        self.assertEqual(phylum.kingdom, self.kingdom)
