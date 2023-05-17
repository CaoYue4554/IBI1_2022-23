from openpyxl import Workbook
import re
import xml.dom.minidom

# input the .xml file
DOMtree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMtree.documentElement
goobos = collection.getElementsByTagName("term")


# define recursion to find all is_a
def recursion(id, idlist, islist, counter):  # counter is involved to make sure the counter will not be cleaned every time I recurse.
    if id not in islist:
        return counter
    indices = [i for i in range(len(islist)) if islist[i] == id]  # some have more than one index.
    for pos in indices:
        counter = recursion(idlist[pos], idlist, islist, counter)  # when the original one is found, keep searching the childnodes of this.
        counter += 1
    return counter


# create the .xlsx file
workbook = Workbook()
sheet = workbook.active
sheet.append(["id", "name", "definition", "childnodes"])
is_a_ID = []
is_a = []

for goobo in goobos:
    ID = goobo.getElementsByTagName("id")[0].childNodes[0].data  # get the id
    childnode = goobo.getElementsByTagName("*")
    for node in childnode:
        if node.tagName == "is_a":
            for i in range(len(node.childNodes)):
                is_a_ID.append(ID)
                is_a.append(node.childNodes[i].data)

for goobo in goobos:
    defstr = goobo.getElementsByTagName("defstr")[0].childNodes[0].data
    if re.search("Autophagosome", defstr, flags=re.I) is not None:  # search for all terms including "autophagosome"
        IDauto = goobo.getElementsByTagName("id")[0].childNodes[0].data  # get the id
        name = goobo.getElementsByTagName("name")[0].childNodes[0].data
        childnodes = recursion(IDauto, is_a_ID, is_a, 0)
        sheet.append([IDauto, name, defstr, childnodes])  # write into the .xlsx file'''

workbook.save(filename='go_obo.xlsx')
