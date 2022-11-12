#!/usr/bin/env python3
from sqlite3 import *
import cgi
import sys

sys.stdout.reconfigure(encoding='utf-8')
def add_note_builder(name_company, adress_main_office, hotline_phone_number):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into property_developer(name_company, adress_main_office, hotline_phone_number) 
        values('{name}', '{adress}', '{number}')"""
		data = data_templayt.format(name = name_company, adress = adress_main_office, number = hotline_phone_number)
		cursor.execute(data)

def main():
	form = cgi.FieldStorage()
	name_company = form.getfirst("name_company", "не определен")
	adress_main_office = form.getfirst("adress_main_office", "не определен")
	hotline_phone_number = form.getfirst("hotline_phone_number", "не определено")

	add_note_builder(name_company, adress_main_office, hotline_phone_number)
		
	print('Content-type: text/html\n')
	print("""<!DOCTYPE HTML>
	<html>
	<head>
		<meta charset="utf-8">
		<title>Добавление записи</title>
	</head>
	<body>
		<form action="/Padges/add_node_padges.html">
			<p>Данные внесены</p>
			<button type="submit" >Вернутся назад</button>
		</form>
	</body>
	</html>""")

main()
