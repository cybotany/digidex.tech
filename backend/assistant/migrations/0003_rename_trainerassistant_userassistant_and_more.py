# Generated by Django 5.1 on 2024-09-08 17:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0002_rename_userassistant_trainerassistant_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrainerAssistant',
            new_name='UserAssistant',
        ),
        migrations.AlterModelOptions(
            name='userassistant',
            options={'verbose_name': 'User Chat Bot', 'verbose_name_plural': 'User Chat Bots'},
        ),
        migrations.RenameField(
            model_name='userassistant',
            old_name='trainer',
            new_name='user',
        ),
    ]
