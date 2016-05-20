from django.db import models

class Kingdom(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Phylum(models.Model):
    name = models.CharField(max_length=255, unique=True)

