# -*- coding: utf-8 -*-
from lxml import etree
 
def parseBookXML(xmlFile):
    with open(xmlFile) as fobj:
        xml = fobj.read()
    
    root = etree.fromstring(xml)
 

    for book in root.getchildren():
        print(book[0].text, book[1].text, book[2].text)
            

    
 
 
if __name__ == "__main__":
    parseBookXML("new_builder.xml")