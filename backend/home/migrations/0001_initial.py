# Generated by Django 5.1 on 2024-09-23 18:28

import django.db.models.deletion
import wagtail.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0094_alter_page_locale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'verbose_name': 'home page',
                'verbose_name_plural': 'home pages',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='UserCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.collection')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='collection', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user collection',
                'verbose_name_plural': 'user collections',
            },
        ),
        migrations.CreateModel(
            name='UserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('user_collection', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='page', to='home.usercollection')),
            ],
            options={
                'verbose_name': 'user page',
                'verbose_name_plural': 'user pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
