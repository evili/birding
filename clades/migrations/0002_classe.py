# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 09:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clades', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('phylum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clades.Phylum')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
