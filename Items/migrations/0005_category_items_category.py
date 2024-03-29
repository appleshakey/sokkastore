# Generated by Django 5.0 on 2023-12-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0004_alter_items_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='category',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
