# Generated by Django 3.1.2 on 2020-10-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
