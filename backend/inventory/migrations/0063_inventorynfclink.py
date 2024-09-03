# Generated by Django 5.0.6 on 2024-08-21 21:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0062_remove_inventoryentitypage_tags_and_more'),
        ('nearfieldcommunication', '0019_remove_nfctag_entity_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryNfcLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfc_tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='nearfieldcommunication.nfctag')),
                ('page', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='inventory.inventoryentitypage')),
            ],
        ),
    ]
