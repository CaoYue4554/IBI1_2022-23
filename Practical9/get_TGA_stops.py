import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out = open("TGA_genes.fa","w")
xxflie =xfile.read()
DNAlist = re.split("\n>",xxflie)
DNAlist_2 = []
for item in range(len(DNAlist)):
    items = re.sub(r"dna.+?\n", '', DNAlist[item])  # delete the useless information after the name.
    items = re.sub("\n","",items)  # delete the \n inside the sequence.
    items = re.sub("c","\n",items)  # change lines between the name of the gene and the sequence.
    items = re.sub("^","\n>",items)  # add \n> at the beginning.
    DNAlist_2.append(items)
DNAlist_2[0] = re.sub("^\n>","",DNAlist_2[0])  # delete the \n on the first row.

for lines in DNAlist_2:
    if re.search("TGA$",lines):  # Find TGA
        out.write(lines)

out.close()
