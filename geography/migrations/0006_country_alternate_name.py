# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-15 11:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0005_load_intial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
