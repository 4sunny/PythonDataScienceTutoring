from matplotlib import pyplot as plt
import numpy as np

x = np.random.randn(30)
y = np.random.randn(30)

fig, ax = plt.subplots(1,1,figsize=(20,10))
ax.scatter(x,y)
ax.set_title('My Scatter Plot')
ax.set_xticklabels(ax.get_xticklabels(), rotation=60, ha='right')
ax.set_xlabel("My x Axis")
ax.set_ylabel('My y Axis')
#ax.set_xticks(np.arange(-4,4.5,0.5))
#plt.tight_layout()
plt.savefig('MyFirstScatter.png')
plt.show()

x1 = np.random.randn(30)
y1 = np.random.randn(30)

plt.scatter(x1,y1, c=y1, cmap=plt.cm.cool)
plt.xticks(rotation=45)
plt.title('My Scatter Plot')
plt.xlabel("My x Axis")
plt.ylabel('My y Axis')
plt.colorbar()
#ax.set_xticks(np.arange(-4,4.5,0.5))
#plt.savefig('MyFirstScatter.png')
plt.show()
















m = [[58.4, 42.1, 34.0, 29.3, 26.1, 24.0, 22.5, 21.3, 20.4, 19.6], [74.6, 44.8, 29.3, 20.9, 16.0, 12.8, 10.6, 9.09, 7.93, 7.03], [82.6, 62.0, 38.3, 24.0, 16.1, 11.4, 8.53, 6.59, 5.24, 4.28], [87.4, 72.2, 54.4, 34.5, 21.3, 13.6, 9.23, 6.52, 4.8, 3.63], [90.5, 79.0, 65.3, 49.4, 32.1, 19.7, 12.2, 7.98, 5.45, 3.83], [92.7, 83.7, 73.0, 60.4, 45.8, 30.3, 18.7, 11.4, 7.26, 4.78], [94.2, 87.1, 78.5, 68.3, 56.6, 43.1, 29.1, 18.0, 11.0, 6.77], [95.4, 89.7, 82.7, 74.4, 64.7, 53.5, 41.0, 28.1, 17.6, 10.6], [96.3, 91.6, 85.9, 79.0, 71.0, 61.7, 51.1, 39.3, 27.2, 17.3], [97.0, 93.2, 88.4, 82.7, 75.9, 68.1, 59.2, 49.1, 37.9, 26.6]]

matrix = np.array(m)
#np.savetxt('matrix.csv', matrix, delimiter=',', fmt="%g")

'''plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = False
plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.set_aspect('equal')
plt.imshow(matrix, interpolation='nearest', cmap=plt.cm.cool, extent=(0.5, 10.5, 10.5, 0.5))
plt.colorbar()
plt.xticks(numpy.arange(1,11))
plt.yticks(numpy.arange(1,11))
plt.clim(100,0)
ax.xaxis.set_label_position('top')
plt.title('Likelihood of Attacker Taking Territory in a Risk Dice Battle')
plt.ylabel('Attacker Dice Count')
plt.xlabel('Defender Dice Count')
for i in range(10):
    for j in range(10):
        plt.text(j + 1, i + 1, str(matrix[i][j]) + "%", va='center', ha='center')
plt.savefig('mygraph.png')
plt.show()'''
