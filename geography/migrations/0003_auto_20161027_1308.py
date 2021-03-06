# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 13:08
from __future__ import unicode_literals

import os
import csv

from django.db import migrations, connections


fixture_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../fixtures'))
csvfilename = os.path.join(fixture_dir, '0003_countries_regions.csv')


def load_fixture(apps, schema_editor):
    if connections.databases['default']['NAME'][:4] == 'test':
        return

    Country = apps.get_model('geography', 'Country')
    Region = apps.get_model('geography', 'Region')

    Country.objects.all().delete()
    Region.objects.all().delete()

    with open(csvfilename, 'rt') as csvfile:
        # Loop over the CSV file getting the new countries
        reader = csv.reader(csvfile)
        for row in reader:
            region_name = row[1]
            country_name = row[0]
            region, created = Region.objects.get_or_create(name=region_name)
            Country.objects.create(name=country_name, region=region)


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0002_load_intial_data'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
