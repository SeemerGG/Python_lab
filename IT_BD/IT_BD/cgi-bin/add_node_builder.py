#!/usr/bin/env python3
from sqlite3 import *
import cgi
import sys

sys.stdout.reconfigure(encoding='utf-8')
def add_note_builder(full_name, salary_bulder, id_bulding):
	with connect('architecture.db') as db:
		cursor  = db.cursor()
		data_templayt = """insert into builder(full_name, salary, id_building) values('{name}', {salary}, {id_bulding})"""
		data = data_templayt.format(name = full_name, salary = salary_bulder, id_bulding = id_bulding)
		cursor.execute(data)

def main():
	form = cgi.FieldStorage()
	full_name = form.getfirst("full_name", "Инакентий")
	salary = form.getfirst("salary", 0)
	id_building = form.getfirst("id_building", 0)

	add_note_builder(full_name, salary, id_building)
		
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
