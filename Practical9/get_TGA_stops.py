import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out = open("TGA_genespre.fa","w")
for lines in xfile:
    if re.match("[ATGC]",lines): # make the gene sequences on one line
        lines =re.sub("\n","",lines)
        out.write(lines)
    if re.match(">",lines): # make the gene name shorter, and put it in one line with the genes
        lines = re.sub(r'(>)','\n\\1',lines)
        lines = re.sub(r"(cdna.+?\n)",'',lines) # delete the useless information after the name.
        out.write(lines)

out = open("TGA_genes.fa","w")
fil = open("TGA_genespre.fa")
for lines in fil:
    if re.search("TGA$",lines):
        lines = re.sub('\s','\n',lines)
        out.write(lines)
out.close()
fil = open("TGA_genes.fa")
for lines in fil:
    print(lines)
fil.close()
