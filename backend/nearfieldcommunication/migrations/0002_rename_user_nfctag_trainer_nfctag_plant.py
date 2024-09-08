# Generated by Django 5.1 on 2024-09-08 04:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversity', '0002_plant_inventory'),
        ('nearfieldcommunication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nfctag',
            old_name='user',
            new_name='trainer',
        ),
        migrations.AddField(
            model_name='nfctag',
            name='plant',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nfc_tag', to='biodiversity.plant'),
        ),
    ]
