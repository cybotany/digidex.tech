# Generated by Django 5.1 on 2024-09-18 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventory', '0011_remove_boxitem_unique_box_item_remove_boxitem_plant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boxitem',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(('app_label', 'biodiversity'), ('model', 'Plant')), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]
