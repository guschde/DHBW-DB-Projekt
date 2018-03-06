# Generated by Django 2.0.2 on 2018-03-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0024_auto_20180228_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzende',
            field=models.TimeField(blank=True, null=True, verbose_name='Einsatzende'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Patient',
            field=models.ManyToManyField(blank=True, null=True, to='index.Patient'),
        ),
    ]