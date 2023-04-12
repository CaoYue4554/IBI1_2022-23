stopcode = input("Input your stop code:")
import re
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
out = open("genespre.fa","w")
for lines in xfile:
    if re.match("[ATGC]",lines): # make the gene sequences on one line
        lines =re.sub("\n","",lines)
        out.write(lines)
    if re.match(">",lines): # make the gene name shorter, and put it in one line with the genes
        lines = re.sub(r'(>)','\n\\1',lines)
        lines = re.sub(r"(dna.+?\n)",'',lines) # in "cdna", I only delete "dna" because I need the "c" to help me locate the end of gene name line.
        out.write(lines)
out.close()

if stopcode == "TGA":
    out = open("TGA_genes.fa","w")
    fil = open("genespre.fa")
    for lines in fil:
        if re.search("TGA$",lines):
            lines = re.sub(r'(c)','P\n',lines) # use "c" to find the end and change lines
            lines = re.sub(r'(P)',str(stops('TGA',lines)),lines) # use the P to input my stop code.
            out.write(lines)
    out.close() # It is now stored in the file.

if stopcode == "TAA":
    out = open("TAA_genes.fa","w")
    fil = open("genespre.fa")
    for lines in fil:
        if re.search("TAA$",lines):
            lines = re.sub(r'(c)','P\n',lines)
            lines = re.sub(r'(P)',str(stops('TAA',lines)),lines)
            out.write(lines)
    out.close() # It is now stored in the file.

if stopcode == "TAG":
    out = open("TAG_genes.fa","w")
    fil = open("genespre.fa")
    for lines in fil:
        if re.search("TAG$",lines):
            lines = re.sub(r'(c)','P\n',lines)
            lines = re.sub(r'(P)',str(stops('TAG',lines)),lines)
            out.write(lines)
    out.close() # It is now stored in the file.
