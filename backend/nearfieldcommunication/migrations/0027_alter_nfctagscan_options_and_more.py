# Generated by Django 5.0.6 on 2024-08-27 06:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0082_remove_box_url_remove_entity_url'),
        ('nearfieldcommunication', '0026_nfctag_entity_delete_nfctagentitylink'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nfctagscan',
            options={'verbose_name': 'nfc tag scan', 'verbose_name_plural': 'nfc tag scans'},
        ),
        migrations.AddIndex(
            model_name='nfctag',
            index=models.Index(fields=['serial_number', 'uuid'], name='nearfieldco_serial__6c76a7_idx'),
        ),
        migrations.AddIndex(
            model_name='nfctagscan',
            index=models.Index(fields=['counter'], name='nearfieldco_counter_596e66_idx'),
        ),
    ]
