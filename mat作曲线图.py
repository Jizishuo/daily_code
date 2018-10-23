from matplotlib import pyplot as plt

'''fig = plt.figure(figsize=[13.44, 7.5], facecolor=(235 / 255, 235 / 255, 235 / 255))
ax1 = fig.add_subplot(1, 1, 1, facecolor=(235 / 255, 235 / 255, 235 / 255))
plt.yticks(range(0, 4, 1), fontsize=14)#设置y轴的的刻度
ax1.barh(height=0.5, width=0.1, y=1, color=(243 / 255, 133 / 255, 36 / 255))
ax1.barh(height=0.5, width=0.2, y=2, color=(243 / 255, 133 / 255, 36 / 255))
ax1.barh(height=0.5, width=0.3, y=3, left=0.1, color=(243 / 255, 133 / 255, 36 / 255))'''
# 柱状图用bar,条形就是barh
# 在barh中，控制条形位置和大小的参数主要是height,width，y和lef
# 而width控制的是长度，也就是横向的宽度
# y值控制着条形图中线在y轴的位置，
# left控制从左边起，那个位置开始画
# plt.show()

'''fig = plt.figure(figsize=[13.44, 7.5], facecolor=(235 / 255, 235 / 255, 235 / 255))
ax1 = fig.add_subplot(1, 1, 1, facecolor=(235 / 255, 235 / 255, 235 / 255), projection='polar')
plt.yticks(range(0, 5, 1), fontsize=14)  # 设置y轴的的刻度
ax1.barh(height=0.5, width=0.1, y=1, color=(243 / 255, 133 / 255, 36 / 255))
ax1.barh(height=0.5, width=1, y=2, color=(243 / 255, 133 / 255, 36 / 255))
ax1.barh(height=0.5, width=1, y=3, color=(243 / 255, 133 / 255, 36 / 255))
ax1.barh(height=0.5, width=1, y=4, color=(243 / 255, 133 / 255, 36 / 255))
plt.show()'''

'''fig = plt.figure(figsize=[13.44,7.5],facecolor=(235/255,235/255,235/255))
ax1=fig.add_subplot(1,1,1,facecolor=(235/255,235/255,235/255),projection='polar')
plt.yticks(range(0,5,1), fontsize=14)#设置y轴的的刻度

ax1.barh(height=0.05,width=1,y=2,color=(243/255,133/255,36/255))
ax1.scatter(x=1,y=2,color=(243/255,133/255,36/255))
ax1.barh(height=0.05,width=1,y=3,color=(243/255,133/255,36/255))
ax1.scatter(x=1,y=3,color=(243/255,133/255,36/255))
ax1.barh(height=0.05,width=1,y=4,color=(243/255,133/255,36/255))
ax1.scatter(x=1,y=4,color=(243/255,133/255,36/255))
plt.show()'''




import numpy as np

fig = plt.figure(figsize=[13.44,7.5],facecolor=(235/255,235/255,235/255))
ax1=fig.add_subplot(1,1,1,facecolor=(235/255,235/255,235/255),projection='polar')
ax1.axis('off')


ax1.barh(height=0.005,width=-0.4*3,y=0.4,color=(243/255,133/255,36/255))
ax1.scatter(-0.4*3,0.4,color=(243/255,133/255,36/255))

ax1.barh(height=0.005,width=-0.5*3,y=0.5,color=(243/255,10/255,36/255))
ax1.scatter(-0.5*3,0.5,color=(243/255,10/255,36/255))

ax1.barh(height=0.005,width=-2*2,y=0.6,color=(243/255,133/255,36/255))
ax1.scatter(-2*2,0.6,color=(243/255,133/255,36/255))

ax1.barh(height=0.005,width=-0.5*np.pi*2,y=0.7,color=(243/255,133/255,36/255))
ax1.scatter(-0.5*np.pi*2,y=0.7,color=(243/255,133/255,36/255))
plt.show()