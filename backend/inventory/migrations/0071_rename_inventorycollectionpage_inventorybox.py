# Generated by Django 5.0.6 on 2024-08-25 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0070_alter_inventoryentitypage_options_and_more'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InventoryCollectionPage',
            new_name='InventoryBox',
        ),
    ]
