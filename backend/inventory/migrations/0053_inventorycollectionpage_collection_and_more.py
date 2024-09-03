# Generated by Django 5.0.6 on 2024-08-18 17:12

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0052_delete_inventoryentity_delete_userinventory_and_more'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorycollectionpage',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection'),
        ),
        migrations.AddField(
            model_name='inventorycollectionpage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='inventoryentitypage',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection'),
        ),
        migrations.AddField(
            model_name='inventoryentitypage',
            name='description',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.CreateModel(
            name='InventoryUserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
            ],
            options={
                'verbose_name': 'inventory user page',
                'verbose_name_plural': 'inventory user pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]
