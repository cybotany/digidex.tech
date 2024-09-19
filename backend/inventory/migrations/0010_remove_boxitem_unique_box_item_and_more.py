# Generated by Django 5.1 on 2024-09-17 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biodiversity', '0004_rename_updated_at_plant_last_modified'),
        ('inventory', '0009_rename_last_updated_box_last_modified_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='boxitem',
            name='unique_box_item',
        ),
        migrations.RemoveField(
            model_name='boxitem',
            name='nfc_tag',
        ),
        migrations.AddConstraint(
            model_name='boxitem',
            constraint=models.UniqueConstraint(fields=('box', 'plant'), name='unique_box_item'),
        ),
    ]
