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

def parse_xml(filename):
    with open(filename) as fobj:
        xml = fobj.read()
    root = etree.fromstring(xml)

    for obj in root.getchildren():
        if obj.tag == "builder":
            add_note_builder(obj[0].text, int(obj[1].text), int(obj[2].text))

def main():
    form = cgi.FieldStorage()
    fileitem = form["filename"]
    if fileitem.filename:
        fn = os.path.basename(fileitem.filename)
        f = open(fn, 'wb')
        f.write(fileitem.file.read())
        parse_xml(fn)
        message = 'The file "' + fn + '" was uploaded successfully'
    else:
        message = 'No file was uploaded'
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="cp1251">
        <title>Загрузка файла</title>
    </head>
    <body>
        <p>%s</p>
    </body>
    </html>
     """ % (message,))

sys.stdout.reconfigure(encoding='utf-8')
main()
