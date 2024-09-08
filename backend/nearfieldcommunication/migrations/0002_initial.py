# Generated by Django 5.1 on 2024-09-08 23:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nearfieldcommunication', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='nfctagscan',
            name='scanned_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='nfctag',
            name='nfc_tag_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tags', to='nearfieldcommunication.nfctagtype'),
        ),
    ]