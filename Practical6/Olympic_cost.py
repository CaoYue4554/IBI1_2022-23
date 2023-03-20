import numpy as np
import matplotlib.pyplot as plt
cost=[1,8,15,7,5,14,43,40]
cost=sorted(cost)
print(cost)
cost=sorted(cost,reverse=True)
print(cost)
N=8
ind=np.arange(N)
width=0.6
p1 =plt.bar(ind,cost,width,color=['red','green','blue','yellow','black','pink','purple','grey'])
plt.ylabel('costs/$billions')
plt.title('Olympic costs')
plt.xticks(ind,('Beijing2008','London2012','Barcelona1992','Athens2004','Seoul1988','Atlanta1996','Sydney2000','LA1984'),fontsize=6)
plt.yticks(np.arange(0,21,10))
plt.show()
