# Generated by Django 5.1 on 2024-09-17 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversity', '0002_plant_nfc_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plant',
            name='nfc_tag',
        ),
    ]