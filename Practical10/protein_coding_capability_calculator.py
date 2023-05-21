import re
def codecap(DNA):
    DNA_change = re.sub("ATG.*?TGA","",DNA,flags=re.IGNORECASE)
    percentage = 1-(len(DNA_change)+6)/len(DNA)
    if percentage > 0.5:
        print(percentage*100,"%","protein-coding")
    elif percentage <0.1:
        print(percentage*100,"%","non-coding")
    else:
        print(percentage*100,"%","unclear")
    return percentage

DNA = "AAAAtGGGGTGA"
codecap(DNA)
