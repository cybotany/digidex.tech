# Generated by Django 5.1 on 2024-09-17 23:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearfieldcommunication', '0008_remove_nfctag_url_delete_nfctagmemory'),
    ]

    operations = [
        migrations.CreateModel(
            name='NfcTagMemory',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('integrated_circuit', models.CharField(choices=[('213', 'NTAG 213'), ('215', 'NTAG 215'), ('216', 'NTAG 216')], default='213', max_length=5)),
                ('memory', models.BinaryField(max_length=888)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('nfc_tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='memory', to='nearfieldcommunication.nfctag')),
            ],
            options={
                'verbose_name': 'nfc tag memory',
                'verbose_name_plural': 'nfc tag memory',
            },
        ),
    ]
