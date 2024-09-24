# Generated by Django 5.1 on 2024-09-24 19:00

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntags', '0003_delete_nfctaglink'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NFCTagMemory',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('eeprom', models.BinaryField(max_length=888)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('ntag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='eeprom', to='ntags.nfctag')),
            ],
            options={
                'verbose_name': 'eeprom',
                'verbose_name_plural': 'eeproms',
            },
        ),
        migrations.CreateModel(
            name='NFCTagScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('scanned_at', models.DateTimeField(auto_now_add=True)),
                ('ntag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scans', to='ntags.nfctag')),
                ('scanned_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'scan',
                'verbose_name_plural': 'scans',
            },
        ),
    ]