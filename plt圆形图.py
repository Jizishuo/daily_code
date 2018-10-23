import numpy as np
from matplotlib import pyplot as plt

year = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
data1 = [1200, 1600, 2400, 3300, 3300, 3800, 4000]
data2 = [0, 0, 100, 275, 400, 480, 580]
radius1 = [np.sqrt(i) for i in data1]
radius2 = [np.sqrt(i) for i in data2]
x = [radius1[0]]

for i in range(len(radius1)):
    try:
        x.append(radius1[i] + radius1[i + 1] + x[-1])
    except:
        continue
y = [100 for i in range(0, 7)]
xy = [i for i in zip(x, y)]

fig = plt.figure(figsize=[20, 20], facecolor=(0, 47 / 255, 99 / 255))
ax = fig.add_subplot(1, 1, 1, facecolor=(0, 47 / 255, 99 / 255))
ax.axis('off')
plt.yticks(range(-100, 900, 100), fontsize=14.5)
plt.xticks(range(-100, 900, 100), fontsize=14.5)
for i in range(len(x)):
    circ = plt.Circle(xy=xy[i], radius=radius1[i], color='w')
    ax.add_patch(circ)
for i in range(len(x)):
    circ = plt.Circle(xy=xy[i], radius=radius2[i], color=(58 / 255, 94 / 255, 148 / 255))
    ax.add_patch(circ)
pgon1 = plt.Polygon([[-100, 100], [800, 100], [800, 300], [-100, 300]], color=(0, 47 / 255, 99 / 255))
pgon3 = plt.Polygon([[0, 140], [880, 140]], color='w')  # 白色的线
ax.add_patch(pgon1)
ax.add_patch(pgon3)
for i in range(len(x)):
    plt.text(x=x[i], y=y[i] + 15, s='%s' % year[i], color='w', ha='center', va='bottom', fontsize=14.5)

for i in range(len(x)):
    plt.text(x=x[i], y=y[i] - 0.8 * radius1[i], s='%s' % data1[i], color=(0, 47 / 255, 99 / 255), ha='center',
             va='bottom', fontsize=14.5)

for i in range(len(x)):
    plt.text(x=x[i], y=y[i] - 1.1 * radius2[i], s='%s' % data2[i], color=(0, 47 / 255, 99 / 255), ha='center', va='top',
             fontsize=11.5)

plt.show()
