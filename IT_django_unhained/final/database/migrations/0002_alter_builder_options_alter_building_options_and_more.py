# Generated by Django 4.1.4 on 2022-12-25 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='builder',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='building',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='propertydeveloper',
            options={'managed': False},
        ),
    ]
