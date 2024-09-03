# Generated by Django 5.0.6 on 2024-08-17 08:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearfieldcommunication', '0004_remove_nfcrecord_tag_remove_nfctag_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfctagtype',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nfctagtype',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
