# Generated by Django 4.1.4 on 2022-12-25 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='property_developer',
            fields=[
                ('name_company', models.TextField(primary_key=True, serialize=False)),
                ('adress_main_office', models.TextField()),
                ('hotline_number', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('adress_building', models.TextField()),
                ('type_building', models.TextField()),
                ('name_company', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.property_developer')),
            ],
        ),
        migrations.CreateModel(
            name='builder',
            fields=[
                ('builder_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.TextField()),
                ('salary', models.IntegerField()),
                ('building_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.building')),
            ],
        ),
    ]