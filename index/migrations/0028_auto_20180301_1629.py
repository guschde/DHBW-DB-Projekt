# Generated by Django 2.0.2 on 2018-03-01 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0027_auto_20180301_1607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dienst',
            old_name='Telefonnummer',
            new_name='Funkrufname',
        ),
    ]