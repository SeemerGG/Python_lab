#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlite3 import *
import cgi
import cgitb; cgitb.enable()
import os
import sys
from lxml import etree

def add_note_builder(full_name, salary_bulder, id_bulding):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into builder(full_name, salary, id_building) values('{name}', {salary}, {id_bulding})"""
		data = data_templayt.format(name = full_name, salary = salary_bulder, id_bulding = id_bulding)
		cursor.execute(data)

def add_note_building(adress_building, type_building, name_company):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into building(adress_building, type_building, name_company)
        values('{adress}', '{type_building}', '{name_company}')"""
		data = data_templayt.format(adress = adress_building, type_building = type_building, name_company= name_company)
		cursor.execute(data)

def add_note_property_developer(name_company, adress_main_office, hotline_phone_number):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into property_developer(name_company, adress_main_office, hotline_phone_number)
        values('{name}', '{adress}', '{number}')"""
		data = data_templayt.format(name = name_company, adress = adress_main_office, number = hotline_phone_number)
		cursor.execute(data)

def parse_xml(filename):
    with open(filename) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)

    for obj in root.getchildren():
        if obj.tag == "builder":
            add_note_builder(obj[0].text, int(obj[1].text), int(obj[2].text))
        if obj.tag == "building":
            add_note_building(obj[0].text, obj[1].text, obj[2].text)
        if obj.tag == "property_developer":
            add_note_property_developer(obj[0].text, obj[1].text, obj[2].text)

def main():
    form = cgi.FieldStorage()
    fileitem = form["filename"]
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        f = open(fn, 'wb')
        f.write(fileitem.file.read())
        f.close()
        parse_xml(fn)
        message = 'Файд "' + fn + '" был успешно добавлен.'
    else:
        message = 'Файл не был добавлен.'
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Загрузка файла</title>
    </head>
    <body>
        <p>%s</p>
		<form action="/Padges/begin_padge_form.html">
			<button type="sumbit" style="height:20px;width:200px">Назад</button>
		</form>
    </body>
    </html>
     """ % (message,))

sys.stdout.reconfigure(encoding='utf-8')
main()
