from django.db import models

class BaseName(models.Model):
    name = models.CharField(max_length=255, unique=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Kingdom(BaseName):
    pass

class Phylum(BaseName):
    kingdom = models.ForeignKey(Kingdom)

class Classe(BaseName):
    phylum = models.ForeignKey(Phylum)

