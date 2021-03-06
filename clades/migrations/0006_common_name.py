# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 12:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clades', '0005_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=127)),
                ('locale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clades.Locale')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clades.Species')),
            ],
            options={
                'ordering': ['locale', 'species'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='commonname',
            unique_together=set([('locale', 'species')]),
        ),
    ]
