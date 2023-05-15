from openpyxl import Workbook
import re
import xml.dom.minidom


# input the .xml file
DOMtree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMtree.documentElement
goobos = collection.getElementsByTagName("term")

# create the .xlsx file
file = Workbook()
thisfile = file.active
thisfile.append(["id", "name", "definition", "childnodes"])

for goobo in goobos:
    defstr = goobo.getElementsByTagName("defstr")[0].childNodes[0].data
    if re.search("Autophagosome", defstr, flags=re.I) is not None:  # search for all terms including "autophagosome"
        ID = goobo.getElementsByTagName("id")[0].childNodes[0].data  # get the id
        name = goobo.getElementsByTagName("name")[0].childNodes[0].data
        childnodes = len(goobo.getElementsByTagName("is_a"))
        thisfile.append([ID, name, defstr, childnodes])  # write into the .xlsx file

file.save('go_obo.xlsx')
