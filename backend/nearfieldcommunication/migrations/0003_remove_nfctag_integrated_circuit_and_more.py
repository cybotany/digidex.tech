# Generated by Django 5.1 on 2024-09-09 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nearfieldcommunication', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nfctag',
            name='integrated_circuit',
        ),
        migrations.AddField(
            model_name='nfctagtype',
            name='integrated_circuit',
            field=models.CharField(choices=[('213', 'NTAG 213'), ('215', 'NTAG 215'), ('216', 'NTAG 216')], default='213', max_length=5),
        ),
    ]