from sqlite3 import *

def create_database():
    with connect('architecture.db') as db:
        cursor =  db.cursor()
        querys = [""" create table property_developer(name_company text not null primary key, adress_main_office text, hotline_phone_number text)""", """ create table building(id_building integer not null primary key, adress_building text, type_building text, name_company text not null, foreign key (name_company) references property_developer(name_company))""", """ create table builder(id_builder integer not null primary key, full_name text, salary integer,id_building integer not null, foreign key (id_building) references building(id_building))"""]
        for i in querys:
            cursor.execute(i)


def input_data():
    with connect('architecture.db') as db: 
        cursor = db.cursor()
        data = [""" insert into property_developer values('SSK', 'Krasnodar, Fadeeva street, 214', '88002223550')""", """ insert into property_developer values('NVM', 'Krasnodar, 2th-Yamalskaya street, 1', '89612121741')""",""" insert into property_developer values('DOSTOYANIE', 'Rostov-on-Don, Filimonovskaya, 45', '88632506007')""", """ insert into building values(12, 'Stasovo street, 213', 'residential building', 'DOSTOYANIE')""", """insert into building values(13,'Stavropolskaya street, 34', 'residential building', 'SSK')""", """insert into building values(14, 'Old-Kubanskaya street, 123', 'residential building', 'NVM')""", """ insert into builder values(456,'Ivanov Ivan Ivanovich', 15000, 12)""", """insert into builder values(457, 'Volodeev Aleksandr Alekseevich', 16000, 13)""", """insert into builder values(458, 'Dimitrov Dmitriy Dmitrivich', 36000, 14)"""]
        for i in data:
	        cursor.execute(i)



def get_output_data_about_builder():
    with connect('architecture.db') as db:
        cursor = db.cursor()
        data = ["""select * from builder""", """select * from property_developer""", """select * from building"""]
        for i in data:
            cursor.execute(i)
            print(cursor.fetchall())


def main():
    create_database()
    input_data()
    get_output_data_about_builder()


