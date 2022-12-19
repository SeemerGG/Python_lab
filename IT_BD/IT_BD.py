from sqlite3 import *

def create_database():
    with connect('architecture.db') as db:
        cursor =  db.cursor()
        querys = [""" create table property_developer(name_company text not null primary key, adress_main_office text, hotline_phone_number text)""",
		""" create table building(id_building integer primary key autoincrement not null, adress_building text, type_building text, name_company text not null, foreign key (name_company) references property_developer(name_company))""", 
		""" create table builder(id_builder integer primary key autoincrement, full_name text, salary integer,id_building integer not null, foreign key (id_building) references building(id_building))"""]
        for i in querys:
            cursor.execute(i)


def input_data():
    with connect('architecture.db') as db: 
        cursor = db.cursor()
        data = [""" insert into property_developer values('SSK', 'Krasnodar, Fadeeva street, 214', '88002223550')""",
		""" insert into property_developer values('NVM', 'Krasnodar, 2th-Yamalskaya street, 1', '89612121741')""",
		""" insert into property_developer values('DOSTOYANIE', 'Rostov-on-Don, Filimonovskaya, 45', '88632506007')""",
		""" insert into building(adress_building, type_building, name_company) values('Stasovo street, 213', 'residential building', 'DOSTOYANIE')""",
		"""insert into building(adress_building, type_building, name_company) values('Stavropolskaya street, 34', 'residential building', 'SSK')""", 
		"""insert into building(adress_building, type_building, name_company) values('Old-Kubanskaya street, 123', 'residential building', 'NVM')""",
        """insert into builder(full_name, salary, id_building) values('Ivanov Ivan Ivanovich', 36000, 1)""",
        """insert into builder(full_name, salary, id_building) values('Sirgay Antonovich Driche', 36000, 2)""",
        """insert into builder(full_name, salary, id_building) values('Ivanov Ivan Daichev', 30000, 3)"""]
        for i in data:
	        cursor.execute(i)   



def get_output_data_about_builder():
    with connect('architecture.db') as db:
        cursor = db.cursor()
        data = ["""select * from builder""", """select * from property_developer""", """select * from building"""]
        for i in data:
            cursor.execute(i)
            print(cursor.fetchall())



create_database()
input_data()


