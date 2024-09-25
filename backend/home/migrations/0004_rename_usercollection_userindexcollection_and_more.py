# Generated by Django 5.1 on 2024-09-25 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_userpage_nfc_tags_userpage_nfc_tag_and_more'),
        ('ntags', '0004_nfctagmemory_nfctagscan'),
        ('wagtailcore', '0094_alter_page_locale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserCollection',
            new_name='UserIndexCollection',
        ),
        migrations.RenameModel(
            old_name='UserPage',
            new_name='UserIndexPage',
        ),
    ]