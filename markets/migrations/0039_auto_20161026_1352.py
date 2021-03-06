# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-26 13:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0038_auto_20161020_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='registration_fees_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='markets_market_registration_fees_currency', to='markets.Currency'),
        ),
        migrations.AlterField(
            model_name='market',
            name='membership_fees',
            field=models.FloatField(default=0, verbose_name='Pricing/Fees - Membership fees'),
        ),
        migrations.RemoveField(
            model_name='market',
            name='registration_fees',
        ),
        migrations.AddField(
            model_name='market',
            name='registration_fees',
            field=models.FloatField(default=0, verbose_name='Pricing/Fees - Registration'),
        ),
    ]
