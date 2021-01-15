from django.conf import global_settings
from django.conf import settings
from django.db import models
from django.utils.translation import get_language
from django.core.exceptions import ObjectDoesNotExist


class BaseNameManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)

class BaseName(models.Model):
    objects = BaseNameManager()

    name = models.CharField(max_length=255, unique=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)

    class Meta:
        abstract = True
        ordering = ['name']


class Kingdom(BaseName):
    pass


class Phylum(BaseName):
    kingdom = models.ForeignKey(Kingdom, on_delete=models.PROTECT)


class Classe(BaseName):
    phylum = models.ForeignKey(Phylum, on_delete=models.PROTECT)


class Ordo(BaseName):
    classe = models.ForeignKey(Classe, on_delete=models.PROTECT)


class Family(BaseName):
    ordo = models.ForeignKey(Ordo, on_delete=models.PROTECT)


class Genus(BaseName):
    family = models.ForeignKey(Family, on_delete=models.PROTECT)


class LocaleManager(models.Manager):
    """Model Manger for available Locales"""

    def get_by_natural_key(self, locale):
        return self.get(locale=locale)

    @staticmethod
    def enabled_locales():
        """Work with enabled languages only."""
        return list(zip(*settings.LANGUAGES))[0]

    def get_queryset(self):
        return super().get_queryset().filter(
                locale__in=self.enabled_locales())


class Locale(models.Model):
    """Locale are the language code for the Species Common Names"""
    locale = models.CharField(max_length=15, 
                              choices=global_settings.LANGUAGES,
                              unique=True)
    objects = LocaleManager()
    
    def natural_key(self):
        return (self.locale,)


class Species(BaseName):
    """Species s one of the basic units of biological classification and a
    taxonomic rank. A species is often defined as a group of organisms capable
    of interbreeding and producing fertile offspring.
    """
    genus = models.ForeignKey(Genus, on_delete=models.PROTECT)

    def sci_name(self):

        """Scientific name of the especies. It's formed by the capitalized
        Genus name followed by the proper name.
        """

        return self.genus.name.capitalize()+u' '+self.name.lower()

    def __str__(self):
        """Return the Common Name of the Species in the current Locale. If
        there is not a Common Name, return the Scientific Name.
        """
        cn = self.sci_name()

        loc = get_language()

        try:
            lang = Locale.objects.get(locale=loc)
        except ObjectDoesNotExist:
            loc = loc.replace('-', '_').split('_')[0]
            try:
                lang = Locale.objects.get(locale=loc)
            except ObjectDoesNotExist:
                lang, created = Locale.objects.get_or_create(locale='en')

        try:
            cn = self.commonname_set.get(locale=lang).cname
        except ObjectDoesNotExist:
            pass

        return cn


    class Meta:
        ordering = ['genus', 'name']
        verbose_name_plural = 'species'


class CommonName(models.Model):
    """A Common Name for any Species in some language. For simplicity,
    there should be only one Common Name for a given Species in a
    given Language.
    """

    cname = models.CharField(max_length=127)
    species = models.ForeignKey(Species, on_delete=models.PROTECT)
    locale = models.ForeignKey(Locale, on_delete=models.PROTECT)

    def __str__(self):
        return u'{0} ({1})'.format(self.cname, self.species.sci_name())

    class Meta:
        ordering = ['locale', 'species']
        unique_together = ['locale', 'species']
