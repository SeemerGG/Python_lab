# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Builder(models.Model):
    id_builder = models.AutoField(primary_key=True, blank=True, null=False)
    full_name = models.TextField(blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    id_building = models.ForeignKey('Building', models.DO_NOTHING)

    


class Building(models.Model):
    id_building = models.AutoField(primary_key=True)
    adress_building = models.TextField(blank=True, null=True)
    type_building = models.TextField(blank=True, null=True)
    name_company = models.ForeignKey('PropertyDeveloper', models.DO_NOTHING)

    


class PropertyDeveloper(models.Model):
    name_company = models.TextField(primary_key=True)
    adress_main_office = models.TextField(blank=True, null=True)
    hotline_phone_number = models.TextField(blank=True, null=True)

    
