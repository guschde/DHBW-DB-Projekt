# Generated by Django 2.0 on 2018-02-08 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0016_auto_20180208_0102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vorfall',
            name='Dienst',
        ),
        migrations.AddField(
            model_name='vorfall',
            name='Hilfstabelle4',
            field=models.ManyToManyField(to='index.Dienst'),
        ),
    ]
