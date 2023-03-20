'''
sort the data in both directions.
Make a bar plot
'''
import numpy as np
import matplotlib.pyplot as plt
cost=[1,8,15,7,5,14,43,40]
cost=sorted(cost)
#This is from the smallest to largest
print(cost)
cost=sorted(cost,reverse=True)
#This is the reverse
print(cost)
N=8

ind=np.arange(N)
#This means from 1 to 8, matching the x labels.
width=0.6
#The width of the bar
p1 =plt.bar(ind,cost,width,color=['red','green','blue','yellow','black','pink','purple','grey'])
plt.ylabel('costs/$billions')
plt.title('Olympic costs')
plt.xticks(ind,('Beijing2008','London2012','Barcelona1992','Athens2004','Seoul1988','Atlanta1996','Sydney2000','LA1984'),fontsize=6)
plt.yticks(np.arange(0,21,10))
#The scope of y axis.In np.arange,the three mean the start, the end, the gap between two lines
plt.show()
#result:
#[1, 5, 7, 8, 14, 15, 40, 43]
#[43, 40, 15, 14, 8, 7, 5, 1]
