# Generated by Django 4.2.5 on 2023-10-03 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_photos_delete_images'),
    ]

    operations = [
        migrations.DeleteModel(
            name='photos',
        ),
    ]