# Generated by Django 2.0 on 2018-02-07 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_auto_20180207_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dienst',
            name='Dienstdatum',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='einsatz',
            name='Einsatzdatum',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Einsatzdatum'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzbeginn',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='time published'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzdatum',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Einsatzdatum'),
        ),
    ]