import re
def stops(stopcode,seq):
    posss = int(seq.find("ATG") + 3) # Find the earliest ATG. +3 to make sure ATG will not overlap with the stop code.
    num = len(re.findall(stopcode, seq[posss:]))
    return num

stopcode = input("Input your stop code:")

xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out = open(f"{stopcode}_genes.fa","w")
xxflie =xfile.read()
DNAlist = re.split("\n>",xxflie)
DNAlist_2 = []
for item in range(len(DNAlist)):
    items = re.sub(r"na.+?\n", '', DNAlist[item])  # delete the useless information after the name.
    items = re.sub("\n","",items)  # delete the \n inside the sequence.
    items = re.sub("d","\n",items)  # change lines between the name of the gene and the sequence.
    items = re.sub("^","\n>",items)  # add \n> at the beginning.
    DNAlist_2.append(items)
DNAlist_2[0] = re.sub("\n>", "", DNAlist_2[0]) # delete the \n on the first row.

for i in range(len(DNAlist_2)):  # delete the \n at the beginning of each line. When they find the first one, quit.
    if re.search(f"{stopcode}$",DNAlist_2[i]):
        DNAlist_2[i] = re.sub("^\n", "", DNAlist_2[i])
        break

for lines in DNAlist_2:
    if re.search(f"{stopcode}$",lines):
        lines = re.sub('c',str(stops(stopcode,lines)),lines)  # use the c to input my coding sequence.
        out.write(lines)
out.close()  # It is now stored in the file.
