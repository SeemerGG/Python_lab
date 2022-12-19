#!/usr/bin/env python3
from sqlite3 import *
import cgi
import sys

sys.stdout.reconfigure(encoding='utf-8')
def add_note_builder(adress_building, type_building, name_company):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into building(adress_building, type_building, name_company) 
        values('{adress}', '{type_building}', '{name_company}')"""
		data = data_templayt.format(adress = adress_building, type_building = type_building, name_company= name_company)
		cursor.execute(data)

def main():
	form = cgi.FieldStorage()
	adress = form.getfirst("adress", "не определен")
	type_building = form.getfirst("type_building", "не определен")
	name_company = form.getfirst("name_company", "не определено")

	add_note_builder(adress, type_building, name_company)
		
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
