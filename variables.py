a=-3.19
#Edinburgh longitude
b=-118.24
#LA logitude
c=116.39
#Haining longitude
d=a-b
print(d)
#LA and Edinburgh
e=c-a
#Haining and Edinburgh
if d>e:
 print("The trip to LA is further")
elif d<e:
 print("The trip to Haining is further")
#e is greater. The trip to Haining is further.

X=True
Y=False
W=X and Y
print(W)
Z=X or Y
print(Z)
#W is False. Z is True.
