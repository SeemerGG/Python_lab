from django.db import models

# Create your models here.
class property_developer(models.Model):
    name_company = models.TextField(primary_key=True)
    adress_main_office = models.TextField()
    hotline_number = models.TextField()

class building(models.Model):
    building_id = models.AutoField(primary_key=True)
    adress_building = models.TextField()
    type_building = models.TextField()
    name_company= models.IntegerField()

class builder(models.Model):
    builder_id = models.AutoField(primary_key=True)
    full_name = models.TextField()
    salary = models.IntegerField()
    builder_id = models.IntegerField()