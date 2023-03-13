#Rabbits=2, generation=1
#while rabbits <100,
# generation+=1
# rabbits*=2
# newborn rabbits=rabbits/2
# print(newborn rabbits)
# loop over
# print the generation that rabbits exceed 100.



Rabbits=2
generation=1
while Rabbits <100:
  generation+=1
  Rabbits*=2
  newborn_rabbits=Rabbits/2
  print(newborn_rabbits)

next_generation=str(generation)

print("The rabbits will exceed 100 in the %sth generation." %next_generation)



#results:
#2.0
#4.0
#8.0
#16.0
#32.0
#64.0
#The rabbits will exceed 100 in the 7th generation.
