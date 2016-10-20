# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-14 15:39
from __future__ import unicode_literals

import os
import csv

from django.conf import settings
from django.db import migrations, connections
from django.core.management import call_command


category_mapping = {
    'Accessories': ['Clothing & Accessories'],
    'Antiques and collectables': ['Furniture, Business & Industrial', 'Clothing & Accessories'],
    'Arts and Crafts': ['Arts & Entertainment', 'Religious & Cermonial'],
    'Automotive': ['Vehicles & Parts'],
    'Baby and Toddler': ['Baby & Toddler'],
    'Clothing and Fashion': ['Clothing & Accessories'],
    'Electronics': ['Camera & Optics', 'Electronics'],
    'Food and Drink': ['Food', 'Beverages & Tobacco'],
    'Health and Beauty': ['Health & Beauty'],
    'Home and Garden': ['Home & Garden', 'Furniture'],
    'Media and Entertainment': ['Media', 'Arts & Entertainment', 'Software'],
    'Sports and Leisure': ['Sporting Goods'],
    'Stationary and Office': ['Business & Industrial', 'Office Supplies'],
    'Tools and Electrical': ['Hardware'],
    'Toys, Games and Models': ['Toys & Games'],
    'Travel': ['Lugguage & Bags', 'Sporting Goods']
}

csvfilename = os.path.join(settings.BASE_DIR, 'products', 'fixtures', '0005_taxonomy.csv')


def migrate_categories(apps, schema_editor):
    if connections.databases['default']['NAME'][:4] == 'test':
        return

    Category = apps.get_model('products', 'Category')
    Market = apps.get_model('markets', 'Market')

    old_relationships = {}
    for category in Category.objects.all():
        old_relationships[category.name] = [market.id for market in category.market_set.all()]

    Category.objects.all().delete()

    with open(csvfilename, 'rt') as csvfile:
        # Loop over the CSV file getting the new Categories
        reader = csv.reader(csvfile)
        for row in reader:
            if row[2] == '':
                # Column 3 is empty, which means it is a new category
                new_category = Category(pk=row[0], name=row[1])
                new_category.save()

    for old_category_name, new_category_names in category_mapping.items():
        try:
            market_links = old_relationships[old_category_name]
        except KeyError:
            continue

        new_categories = Category.objects.filter(name__in=new_category_names)

        for market in Market.objects.filter(id__in=market_links):
            for new_category in new_categories:
                market.product_categories.add(new_category)


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_load_intial_data'),
        ('markets', '0026_load_intial_data'),
    ]

    operations = [
        migrations.RunPython(migrate_categories),
    ]
