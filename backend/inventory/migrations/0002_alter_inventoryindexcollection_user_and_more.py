# Generated by Django 5.1 on 2024-10-08 21:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryindexcollection',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='index_collection', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventoryindexpage',
            name='user_collection',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page', to='inventory.inventoryindexcollection'),
        ),
    ]
