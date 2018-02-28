# Generated by Django 2.0 on 2018-02-28 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0022_auto_20180228_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rettungsmittel',
            name='id',
        ),
        migrations.AlterField(
            model_name='ansprechpartner',
            name='Geschlecht',
            field=models.CharField(choices=[('w', 'W'), ('m', 'M')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Alter',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Geschlecht',
            field=models.CharField(choices=[('w', 'W'), ('m', 'M')], default='W', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Name',
            field=models.CharField(default='Musterfrau', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Vorname',
            field=models.CharField(default='Patientin', max_length=20),
        ),
        migrations.AlterField(
            model_name='rettungsmittel',
            name='Bezeichnung',
            field=models.CharField(max_length=30, primary_key='true', serialize=False),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Triagekategorie',
            field=models.CharField(choices=[('leichte Verletzungen', 'LEICHTE VERLETZUNGEN'), ('mittlere Verletzungen', 'MITTLERE VERLETZUNGEN'), ('schwere Verletzungen', 'SCHWERE VERLETZUNGEN')], default='LEICHTE VERLETZUNGEN', max_length=21, verbose_name='Triagekategorie'),
        ),
    ]
