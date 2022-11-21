#!/usr/bin/env python3
from sqlite3 import *
import cgi
import sys

sys.stdout.reconfigure(encoding='utf-8')

def show_note_builder():

    with connect('architecture.db') as db:
        cursor  = db.cursor()
        data = """select * from builder"""
        cursor.execute(data)
        records = cursor.fetchall()
        for row in records:
            print("<p>Номер сотрудника {} </p>".format(row[0]))
            print("<p>ФИО {} </p>".format(row[1]))
            print("<p>Зарплата {} </p>".format(row[2]))
            print("<p>Номер стройки {} </p><p></p>".format(row[3]))




print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
	<html>
	<head>
		<meta charset="utf-8">
		<title>Добавление записи</title>
	</head>
	<body>""")
show_note_builder()
print("""<p>Данные внесены</p>
        <form action="/cgi-bin/xml_print_bulder.py">
			<button type="submit" >Вывод в xml</button>
            <p></p>
		</form>""")
print("""<form action="/Padges/show_date_padges.html">
			<button type="submit" >Вернутся назад</button>
		</form>
	</body>
	</html>""")
