# Generated by Django 5.1 on 2024-10-03 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_userindexcollection_collection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userindexpage',
            name='user_collection',
        ),
        migrations.RemoveField(
            model_name='userindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='UserIndexCollection',
        ),
        migrations.DeleteModel(
            name='UserIndexPage',
        ),
    ]