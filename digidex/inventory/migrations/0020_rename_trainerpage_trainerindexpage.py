# Generated by Django 5.0.6 on 2024-08-08 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0019_trainer_trainerpage'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrainerPage',
            new_name='TrainerIndexPage',
        ),
    ]
