# Generated by Django 5.1 on 2024-09-25 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_usercollection_userindexcollection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userindexpage',
            name='nfc_tag',
        ),
    ]