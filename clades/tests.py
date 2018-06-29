from django.test import TestCase

from .models import Kingdom, Phylum, Classe, Ordo, Family, Genus, Species, CommonName, Locale

_KINGDOM_NAME = u'Animalia'
_PHYLUM_NAME = u'Chordata'
_CLASSE_NAME = u'Aves'
_ORDO_NAME = u'Passeriformes'
_FAMILY_NAME = u'Paridae'
_GENUS_NAME = u'Periparus'
_SPECIES_NAME = u'ater'
_COMMON_NAME = {
    u'ca': u'Mallerenga Petita',
    u'en': u'Coal Tit',
}

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
        (self.ordo, created) = Ordo.objects.get_or_create(
            name=_ORDO_NAME,
            classe=self.classe)
        (self.family, created) = Family.objects.get_or_create(
            name=_FAMILY_NAME,
            ordo=self.ordo)
        (self.genus, created) = Genus.objects.get_or_create(
            name=_GENUS_NAME,
            family=self.family)
        (self.species, created) = Species.objects.get_or_create(
            name=_GENUS_NAME,
            genus=self.genus)
        self.locale = {}
        self.common_name = {}
        for lc, cn in _COMMON_NAME.items():
            print("======================> LOCALE:", lc)
            (self.locale[lc], created) = Locale.objects.get_or_create(locale=lc)
            (self.common_name[lc], created) = CommonName.objects.get_or_create(
                cname=cn,
                locale=self.locale[lc],
                species=self.species
            )

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

class OrdoTest(CladesTest):
    def test_ordo_has_classe(self):
        ordo = Ordo.objects.get(name=_ORDO_NAME)
        self.assertEqual(ordo.classe, self.classe)

class FamilyTest(CladesTest):
    def test_family_has_ordo(self):
        family = Family.objects.get(name=_FAMILY_NAME)
        self.assertEqual(family.ordo, self.ordo)

class GenusTest(CladesTest):
    def test_genus_has_family(self):
        genus = Genus.objects.get(name=_GENUS_NAME)
        self.assertEqual(genus.family, self.family)

class SpeciesTest(CladesTest):
    def test_species_has_genus(self):
        species = Species.objects.get(name=_SPECIES_NAME)
        self.assertEqual(species.genus, self.genus)

class CommonNameTest(CladesTest):
    def test_common_name_has_species(self):
        common_name = CommonName.objects.get(cname=_COMMON_NAME['ca'])
        self.assertEqual(common_name.species, self.species)

    def test_common_name_no_local(self):
             from django.conf import settings
             # set default to a missing cn
             settings.LANGUAGE_CODE = u'eo'
             self.assertEqual(self.species,
                              self.species.sci_name(),
                              'Fallback common name is not scientific name ' % (str(self.species), self.species.sci_name() )
             )
