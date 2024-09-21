# Generated by Django 5.1 on 2024-09-19 21:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('ntags', '0001_initial'),
        ('wagtailcore', '0094_alter_page_locale'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='nfctagmemory',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='locked',
            field=models.BooleanField(default=False, editable=False, verbose_name='locked'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='locked_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='locked at'),
        ),
        migrations.AddField(
            model_name='nfctagmemory',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AlterField(
            model_name='nfctag',
            name='content_type',
            field=models.ForeignKey(blank=True, limit_choices_to=models.Q(models.Q(('app_label', 'accounts'), ('model', 'User')), models.Q(('app_label', 'inventory'), ('model', 'Box')), _connector='OR'), null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
    ]