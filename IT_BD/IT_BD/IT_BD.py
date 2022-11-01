from sqlite3 import *

def create_database():
    with connect('architecture.db') as db:
        cursor =  db.cursor()
        querys = [""" create table property_developer(name_company text not null primary key, adress_main_office text, hotline_phone_number text)""", """ create table building(id_building integer not null primary key, adress_building text, type_building text)""", """ create table builder(id_builder integer not null primary key, full_name text, salary integer,id_building integer not null, foreign key (id_building) references building(id_building))"""]
        for i in querys:
            cursor.execute(i)


def input_data():
    data = [""" insert into property_developer values('SSK', 'Krasnodar, Fadeeva street, 214', '88002223550')""", """ insert into property_developer values('NVM', 'Krasnodar, 2th-Yamalskaya street, 1', '89612121741')""",""" insert into property_developer values('DOSTOYANIE', 'Rostov-on-Don, Filimonovskaya, 45', '88632506007')"""]

input_data()