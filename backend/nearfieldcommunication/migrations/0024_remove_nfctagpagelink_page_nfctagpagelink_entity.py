# Generated by Django 5.0.6 on 2024-08-27 03:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0081_alter_box_url_alter_box_uuid_alter_entity_url_and_more'),
        ('nearfieldcommunication', '0023_remove_nfctagpagelink_owner_nfctag_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfctagpagelink',
            name='page',
        ),
        migrations.AddField(
            model_name='nfctagpagelink',
            name='entity',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nfc_link', to='inventory.entity'),
        ),
    ]
