# Generated by Django 4.1.4 on 2022-12-25 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rename_building_id_builder_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='builder',
            name='building',
            field=models.ForeignKey(db_column='id_building', on_delete=django.db.models.deletion.DO_NOTHING, to='database.building'),
        ),
        migrations.AlterField(
            model_name='building',
            name='property_developer',
            field=models.ForeignKey(db_column='name_company', on_delete=django.db.models.deletion.DO_NOTHING, to='database.property_developer'),
        ),
    ]