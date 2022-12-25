from django.shortcuts import render
from django.http import HttpResponse
from .models import Builder, Building, PropertyDeveloper
import xml.dom.minidom as minidom
# Create your views here.
def index(request):
    return render(request, "index.html")

def create_new_builder(name, sal, id_b):
    Builder.objects.create(full_name = name, salary = sal, id_building = id_b)

def add_builder(request):
    name = request.POST.get("full_name", "Undefined")
    sal = int(request.POST.get("salary", "Undefined"))
    id_b = int(request.POST.get("id_building","Undefined"))

    create_new_builder(name, sal, id_b)
    return HttpResponse("<h2>Запись успешно добавленна!</h2>")

def create_new_building(adress, type, name_c):
    Building.objects.create(adress_building = adress, type_building = type, name_company = name_c)

def add_building(request):
    adress = request.POST.get("adress","Undefined")
    type = request.POST.get("type","Undefined")
    name_company = request.POST.get("name_company", "Undefined")

    create_new_building(adress, type, name_company)
    return HttpResponse("<h2>Запись успешно добавленна!</h2>")
    
def create_new_dev(name, adress, hotline):
    PropertyDeveloper.objects.create(name_company = name, adress_main_office = adress, hotline_phone_number = hotline)

def add_dev(request):
    name = request.POST.get("name_company","Undefined")
    adress = request.POST.get("adress_main_office","Undefined")
    hotline = request.POST.get("hotline_phone_number", "Undefined")

    create_new_dev(name, adress, hotline)
    
    return HttpResponse("<h2>Запись успешно добавленна!</h2>")
