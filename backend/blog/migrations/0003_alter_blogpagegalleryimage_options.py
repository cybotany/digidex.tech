# Generated by Django 5.1 on 2024-10-01 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_blogtagindexpage_tagindexpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpagegalleryimage',
            options={'ordering': ['sort_order'], 'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
    ]