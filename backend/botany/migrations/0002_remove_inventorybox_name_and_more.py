# Generated by Django 5.1 on 2024-09-30 02:56

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botany', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorybox',
            name='name',
        ),
        migrations.AlterField(
            model_name='inventorybox',
            name='description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]