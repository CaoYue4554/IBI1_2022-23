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

# This code will report the percentage without including "ATG" and "TGA"
DNA = "AAAAtGGGGTGA"
print("'ATG' and 'TGA' not included.")
codecap(DNA)
