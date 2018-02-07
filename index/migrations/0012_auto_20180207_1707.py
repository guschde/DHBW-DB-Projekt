# Generated by Django 2.0 on 2018-02-07 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20180207_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ansprechpartner',
            name='Datum',
            field=models.DateTimeField(verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='dienst',
            name='Dienstdatum',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Dienstdatum'),
        ),
        migrations.AlterField(
            model_name='dienst',
            name='Einsatzbeginnzeit',
            field=models.TimeField(verbose_name='Einsatzbeginn'),
        ),
        migrations.AlterField(
            model_name='dienst',
            name='Einsatzendezeit',
            field=models.TimeField(verbose_name='Einsatzende'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Patient_Einsatzdatum',
            field=models.DateTimeField(verbose_name='Behandlungsdatum'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzbeginn',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Einsatzbeginn'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzende',
            field=models.DateTimeField(verbose_name='Einsatzende'),
        ),
    ]
