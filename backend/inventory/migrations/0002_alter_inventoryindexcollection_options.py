# Generated by Django 5.1 on 2024-10-04 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryindexcollection',
            options={'verbose_name': 'index collection', 'verbose_name_plural': 'index collections'},
        ),
    ]