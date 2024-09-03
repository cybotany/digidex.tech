# Generated by Django 5.0.6 on 2024-08-17 23:57

import django.db.models.deletion
import uuid
import wagtail.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0042_remove_inventorycollection_trainer_inventory_and_more'),
        ('wagtailcore', '0093_uploadedfile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryassetpage',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='inventoryassetpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='trainerinventorypage',
            name='collection',
        ),
        migrations.RemoveField(
            model_name='trainerinventorypage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='trainerinventorypage',
            name='trainer',
        ),
        migrations.AlterModelOptions(
            name='collectionentity',
            options={'verbose_name': 'collection entity', 'verbose_name_plural': 'collection entities'},
        ),
        migrations.AlterModelOptions(
            name='inventorycollection',
            options={'verbose_name': 'inventory collection', 'verbose_name_plural': 'inventory collections'},
        ),
        migrations.AlterModelOptions(
            name='userinventory',
            options={'verbose_name': 'user inventory', 'verbose_name_plural': 'user inventories'},
        ),
        migrations.AlterUniqueTogether(
            name='userinventory',
            unique_together={('user', 'slug')},
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='locked',
            field=models.BooleanField(default=False, editable=False, verbose_name='locked'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='locked_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='locked at'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AddField(
            model_name='collectionentity',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='locked',
            field=models.BooleanField(default=False, editable=False, verbose_name='locked'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='locked_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='locked at'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AddField(
            model_name='inventorycollection',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userinventory',
            name='locked',
            field=models.BooleanField(default=False, editable=False, verbose_name='locked'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='locked_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='locked at'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AddField(
            model_name='userinventory',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='collectionentity',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='inventorycollection',
            name='description',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterUniqueTogether(
            name='collectionentity',
            unique_together={('inventory_collection', 'slug')},
        ),
        migrations.AlterUniqueTogether(
            name='inventorycollection',
            unique_together={('user_inventory', 'slug')},
        ),
        migrations.AddIndex(
            model_name='collectionentity',
            index=models.Index(fields=['name'], name='inventory_c_name_0dd4e5_idx'),
        ),
        migrations.AddIndex(
            model_name='inventorycollection',
            index=models.Index(fields=['name'], name='inventory_i_name_92a2e5_idx'),
        ),
        migrations.AddConstraint(
            model_name='collectionentity',
            constraint=models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale_inventory_collectionentity'),
        ),
        migrations.AddConstraint(
            model_name='inventorycollection',
            constraint=models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale_inventory_inventorycollection'),
        ),
        migrations.AddConstraint(
            model_name='userinventory',
            constraint=models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale_inventory_userinventory'),
        ),
    ]
