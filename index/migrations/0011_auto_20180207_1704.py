# Generated by Django 2.0 on 2018-02-07 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20180207_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dienst',
            name='Einsatz_ID',
            field=models.ForeignKey(default='Einsatzleitung', on_delete=django.db.models.deletion.DO_NOTHING, to='index.Einsatz'),
        ),
        migrations.AlterField(
            model_name='dienst',
            name='Personal_ID',
            field=models.ForeignKey(default='Gruppenführer', on_delete=django.db.models.deletion.DO_NOTHING, to='index.Personal'),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzort',
            field=models.CharField(default='Heidenheim', max_length=20),
        ),
    ]
