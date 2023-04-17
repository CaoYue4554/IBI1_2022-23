import re
seq = "TGATAAATGATAATGATGA"
def stops(stops,seq):
    pos = re.findall(stops,seq)
    count = 0
    posss = seq.find("ATG") + 3 # Find the earliest ATG. +3 to make sure ATG will not overlap with the stop code.
    for poss in range(len(pos)):
        sit = posss + 1 # Start searching after ATG, so the stopcode will not appear earlier than ATG.
        if seq.find(stops,sit) != -1:
            posss = seq.find(stops,sit)
            count += 1 # count times
        else:
            break
    return count
codeseq = stops("TAA",seq) + stops("TGA",seq) +stops("TAG", seq)
print(codeseq)
