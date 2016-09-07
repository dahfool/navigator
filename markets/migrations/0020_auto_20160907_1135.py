# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-07 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0019_auto_20160907_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='deposit_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='membership_fees',
            field=models.FloatField(blank=True, default=0, help_text='Converted to GBP', null=True,
                                    verbose_name='Pricing/Fees - Membership fees'),
        ),
        migrations.AlterField(
            model_name='market',
            name='web_traffic',
            field=models.FloatField(blank=True, default=0, help_text='in millions', null=True,
                                    verbose_name='Number of registered users'),
        ),
    ]
