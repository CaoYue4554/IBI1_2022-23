import re
def stops(stopcode,seq):
    posss = int(seq.find("ATG") + 3) # Find the earliest ATG. +3 to make sure ATG will not overlap with the stop code.
    num = len(re.findall(stopcode, seq[posss:]))
    return num
seq = "TGAATGTGATGA"
codeseq = stops("TGA", seq) + stops("TAA", seq) + stops("TAG", seq)
print(codeseq)
