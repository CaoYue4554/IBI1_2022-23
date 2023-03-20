'''
Import matplot
type in the keys and values in pairs, and print.
Use keys as the labels on pie chart, values as the proportion they take up on the plot.
Then type certain keys to show the corresponding value.
'''

import matplotlib.pyplot as plt

movie_genre = {'Comedy':73, 'Action':42, 'Romance':38, 'Fantasy':28, 'Science-fiction':22,'Horror':19,'Cri>
print(movie_genre)

labels=movie_genre.keys()
sizes=movie_genre.values()
plt.pie(x=sizes,explode=None,labels=labels)
plt.show()

print(movie_genre['Comedy'])
#The key can be changed here to get the values of other keys.


#Results:
#{'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': >
#73

