import re
def codecap(DNA):
    DNA_change = re.sub("ATG.+?TGA","",DNA,flags=re.IGNORECASE) #DNA change stores the sequence out of the coding sequence.
    percentage = 1-len(DNA_change)/len(DNA)
    if percentage > 0.5:
        print(percentage,"protein-coding")
    elif percentage <0.1:
        print(percentage,"non-coding")
    else:
        print(percentage,"unclear")
    return percentage

DNA = "AAAAtGGGGTGA"
codecap(DNA)
