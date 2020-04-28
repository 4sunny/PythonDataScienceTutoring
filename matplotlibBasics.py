import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]



# Method 1 = No figures, no axes
plt.plot(x,y)
plt.show()

plt.scatter(x,y)
plt.show()

# Method 2 = Figure with no axes
figure1 = plt.plot(x, y)
#plt.show()

figure2 = plt.scatter(x, y)
plt.show()

# Method 3 Figure with axes *depreciated*
x1 = np.random.rand(10)
y1 = np.random.rand(10)
x2 = np.random.rand(10)
y2 = np.random.rand(10)
x3 = np.random.rand(10)
y3 = np.random.rand(10)
x4 = np.random.rand(10)
y4 = np.random.rand(10)


figure = plt.figure()
ax1 = figure.add_subplot(221)
ax1.plot(x1, y1, 'b')
plt.gca().set_title("ax1")
ax2 = figure.add_subplot(122)
ax2.plot(x2, y2,'k')
ax2.set_title("ax2")
ax3 = figure.add_subplot(223)
ax3.plot(x3, y3, color='r')
plt.show()

# Method 4 Figure with axes using subplots()
fig, a = plt.subplots(2,2)
#fig, ((axe1, axe2), (axe3, axe4)) = plt.subplots(2,2)
x5 = np.arange(1,5)
y5 = np.arange(1,5)
a[0][0].plot(x5,y5)
a[0][0].set_title('subplot1')
a[0][1].hist(x5,y5)
a[0][1].set_title('subplot2')
a[1][0].plot(x5,y5)
a[1][0].plot(x5,x5*x5)
a[1][0].set_title('subplot3')
a[1][1].scatter(x5,y5)
a[1][1].set_title('subplot4')
plt.show()