# Generated by Django 5.1 on 2024-09-19 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_navigationsettings_logo_basedocument_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basedocument',
            options={'ordering': ['sort_order']},
        ),
        migrations.AlterModelOptions(
            name='baseimage',
            options={'ordering': ['sort_order']},
        ),
        migrations.AddField(
            model_name='basedocument',
            name='caption',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='basedocument',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='baseimage',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]
