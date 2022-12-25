from django.shortcuts import render
from django.http import HttpResponse
import sys
from lxml import etree, objectify
from .models import property_developer, builder, building
import xml.dom.minidom as minidom

# Create your views here.
def index(request):
    return render(request, "index.html")

def add_builder_to_db(name, sal, b_id):
    builder.objects.create(full_name=name,salary = sal, building_id= b_id)

def add_property_dev_to_db(name, adress, hotline):
    property_developer.objects.create(name_company = name, adress_main_office = adress, hotline_number = hotline)

def add_building_to_db(adress, type, name_c):
    building.objects.create(adress_building = adress, type_building = type, name_company = name_c)

def add_builder(request):
    name = request.POST.get("full_name", "Undefined")
    sal = request.POST.get("salary", "Undefined")
    b_id = request.POST.get("building_id", "Undefined")
    data = { "name": name, "sal": sal, "b_id":b_id}

    add_builder_to_db(name, sal, b_id)

    return render(request, "builder_added.html", context=data)

def create_builder(buld, id, full_name, sal, b_id):
    buder= buld.createElement("builder")
    buder.setAtribute("id", str(id))
    buder.setAttribute("full_name", full_name)
    buder.setAttribute("salary", sal)
    buder.setAttribute("building_id", b_id)
    return buder

def download_builder_xml(request):
    bul = minidom.Document()
    root  = bul.createElement("builder")

    q = builder.objects.all()

    for b in q:
        root.appendChild(create_builder(bul, b.builder_id, b.full_name, b.salary, b.building_id))
    
    obj_xml = root.toprettyxml()
    print(obj_xml)
    return HttpResponse(obj_xml, content_type= "text/xml")

def show_builder(request):
    s = []
    q = builder.objects.all()
    for b in q:
        s.append("id:{}, name:{}, salary:{}, building_id{}".format(b.builder_id,b.full_name, b.salary, b.building_id))
    data = { "brs":s }
    return render(request, "show_builders.html", context = data)

def parse_xml(filename):
    xml = filename.read()

    root = minidom.pasreString(xml)
    brs = root.getElementsByTagName("builder")

    for i in brs:
        name = i.getAttribute("full_name")
        salary = i.getAttribute("salary")
        building_id = i.getAttribute("building_id")
        add_builder_to_db(name, salary, building_id)

def upload_builder(request):
    filename = request.FILES['filename']
    parse_xml(filename)
    return show_builder(request)

def add_building(request):
    adress = request.POST.get("adress_building", "Underfined")
    type = request.POST.get("type_building", "Underfined")
    name_company = request.POST.get("name_company", "Underfined")

    data = {
        "name_c": name_company,
        "adress": adress, 
        "type": type
    }

    add_building_to_db(adress, type, name_company)

    return render(request, "building_added.html", context=data)

def add_property_dev(request):
    name_c = request.POST.get("name_company", "Undefined")
    adress = request.POST.get("adress_main_office", "Undefined")
    hotline = request.POST.get("hotline_number", "Undefined")

    data = {
        "name_c": name_c,
        "adress": adress,
        "hotline": hotline
    }
    
    add_property_dev_to_db(name_c, adress, hotline)

    return render(request, "property_dev.html", context=data)
    