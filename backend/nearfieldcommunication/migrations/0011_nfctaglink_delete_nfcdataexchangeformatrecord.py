# Generated by Django 5.0.6 on 2024-08-18 22:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearfieldcommunication', '0010_alter_nfcdataexchangeformatrecord_options_and_more'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='NfcTagLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nfc_tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='nearfieldcommunication.nfctag')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'nfc tag link',
                'verbose_name_plural': 'nfc tag links',
            },
        ),
        migrations.DeleteModel(
            name='NfcDataExchangeFormatRecord',
        ),
    ]
