from django.test import TestCase

from .models import Kingdom, Phylum, Classe, Family

_KINGDOM_NAME = u'Animalia'
_PHYLUM_NAME = u'Chordata'
_CLASSE_NAME = u'Aves'
_FAMILY_NAME = u'Passeriformes'

class CladesTest(TestCase):

    def setUp(self):
        (self.kingdom, created) = Kingdom.objects.get_or_create(
            name=_KINGDOM_NAME)
        (self.phylum, created) = Phylum.objects.get_or_create(
            name=_PHYLUM_NAME,
            kingdom=self.kingdom)
        (self.classe, created) = Classe.objects.get_or_create(
            name=_CLASSE_NAME,
            phylum=self.phylum)
        (self.family, created) = Family.objects.get_or_create(
            name=_FAMILY_NAME,
            classe=self.classe)

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

class ClasseTest(CladesTest):
    def test_classe_has_phylum(self):
        classe = Classe.objects.get(name=_CLASSE_NAME)
        self.assertEqual(classe.phylum, self.phylum)

class FamilyTest(CladesTest):
    def test_family_has_classe(self):
        family = Family.objects.get(name=_FAMILY_NAME)
        self.assertEqual(family.classe, self.classe)
