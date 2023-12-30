# Generated by Django 5.0 on 2023-12-16 11:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0002_items_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='no_link', max_length=100), default=[], size=3),
        ),
    ]