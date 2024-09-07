# Generated by Django 5.1 on 2024-09-07 03:22

import django.db.models.deletion
import modelcluster.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0100_remove_inventoryindex_collection_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryPlant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(editable=False, max_length=250)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('user_inventory', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='plants', to='inventory.userinventory')),
            ],
            options={
                'indexes': [models.Index(fields=['uuid'], name='inventory_i_uuid_9699b6_idx')],
            },
        ),
    ]