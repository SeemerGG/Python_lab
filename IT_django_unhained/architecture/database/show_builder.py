sys.stdout.reconfigure(encoding='utf-8')

def show_note_builder():
    list_br = []
    with connect('architecture.db') as db:
        cursor  = db.cursor()
        data = """select * from builder"""
        cursor.execute(data)
        records = cursor.fetchall()

        for row in records:
            list_br.append(create_br(row[0], row[1], row[2], row[3]))
            print("<p>Номер сотрудника {} </p>".format(row[0]))
            print("<p>ФИО {} </p>".format(row[1]))
            print("<p>Зарплата {} </p>".format(row[2]))
            print("<p>Номер стройки {} </p><p></p>".format(row[3]))
    create_xml_br(list_br)

def create_br(id, full_name, salary, id_bild):
    br = objectify.Element("builder")
    br.id = id
    br.full_name = full_name
    br.salary = salary
    br.id_bild = id_bild
    return br

def create_xml_br(list_br):
    xml = """data"""

    root = objectify.Element(xml)#fromstring(xml)


    for  i in list_br:
        root.append(i)

    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True)

    try:
        with open("show_builder.xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
    except IOError:
        pass



'''print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
	<html>
	<head>
		<meta charset="utf-8">
		<title>Добавление записи</title>
	</head>
	<body>""")
show_note_builder()
print("""<p>Данные внесены</p>
        <form>
        <a href="/show_builder.xml" download="" title="">Скачать в xml</a>
        <p></p>
        </form>""")
print("""<form action="/Padges/show_date_padges.html">
			<button type="submit" >Вернутся назад</button>
		</form>
	</body>
	</html>""")'''