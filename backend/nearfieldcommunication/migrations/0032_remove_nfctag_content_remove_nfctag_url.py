# Generated by Django 5.1 on 2024-09-07 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nearfieldcommunication', '0031_nfctag_content_nfctag_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfctag',
            name='content',
        ),
        migrations.RemoveField(
            model_name='nfctag',
            name='url',
        ),
    ]
