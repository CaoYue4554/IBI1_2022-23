import pandas as pd
import re


def align(seq1, seq2):  # use blosum to score, and then calculate the identical amino acids.
    data = pd.read_excel("BLOSUM.xlsx", index_col="First")  # open BLOSUM.xlsx
    score = 0
    identity = 0
    for n in range(len(seq1)):
        i = seq1[n]
        j = seq2[n]
        score += data.loc[i, j]
        if i == j:
            identity += 1
    return score, identity


def dealfa(file):  # deal with the fasta file. change it into a sequence.
    f = file.read()
    seq = re.sub("^.+?\n", "", f)
    seq = re.sub("\n", "", seq)
    return seq


file1 = open('ACE2_human.fa')
human = dealfa(file1)
file2 = open('ACE2_mouse.fa')
mouse = dealfa(file2)
file3 = open('ACE2_cat.fa')
cat = dealfa(file3)

print("human ,mouse", align(human, mouse))
print("cat, mouse", align(cat, mouse))
print("human, cat", align(human, cat))
