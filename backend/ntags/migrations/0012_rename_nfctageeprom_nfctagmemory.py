# Generated by Django 5.1 on 2024-09-22 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ntags', '0011_remove_nfctag_design_delete_nfctagdesign'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NFCTagEEPROM',
            new_name='NFCTagMemory',
        ),
    ]
