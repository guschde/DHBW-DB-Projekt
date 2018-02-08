# Generated by Django 2.0 on 2018-02-08 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20180207_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vorfall',
            name='Einsatzort',
            field=models.CharField(default='Heidenheim', max_length=50),
        ),
        migrations.AlterField(
            model_name='vorfall',
            name='Patient',
            field=models.ManyToManyField(through='index.Hilfstabelle1', to='index.Patient'),
        ),
    ]
