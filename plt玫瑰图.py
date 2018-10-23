import numpy as np
import matplotlib.pyplot as plt
import random

'''y=20
x=np.pi/2
w=np.pi/2
color=(206/255,32/255,69/255)
edgecolor=(206/255,32/255,69/255)

fig=plt.figure(figsize=(13.44,7.5))#建立一个画布
ax = fig.add_subplot(111,projection='polar')#建立一个坐标系，projection='polar'表示极坐标
ax.bar(left=x, height=y, width=w,bottom=10,color=color,edgecolor=color)'''
#一个柱状图由left，bottom，height，width四个参数决定位置和大小left决定了左边界，
# bottom决定了下边界，height决定了长度，width决定了宽度.
#left决定了扇形的中线位置，然后height决定扇形的长度，bottom决定了下边界，width决定了扇形的宽度

#十个大扇形的位置，思路大概是，把一个圆分成十份，然后找到十个扇形中线对应的θ
#然后在计算20个小扇形的位置
#画第一层，最外圈的放文字的位置,先画个半径是7000，在画个半径是6000，然后
x1 = [np.pi / 10 + np.pi * i / 5 for i in range(1, 11)]
x2 = [np.pi / 20 + np.pi * i / 5 for i in range(1, 11)]
x3 = [3 * np.pi / 20 + np.pi * i / 5 for i in range(1, 11)]
#画第一层，最外圈的放文字的位置,先画个半径是7000，在画个半径是6000，然后
y1 = [7000 for i in range(0, 10)]
y2 = [6000 for i in range(0, 10)]
fig = plt.figure(figsize=(13.44, 7.5))
ax = fig.add_subplot(111, projection='polar')
ax.axis('off')
ax.bar(left=x1, height=y1, width=np.pi / 5, color=(220 / 255, 222 / 255, 221 / 255),
       edgecolor=(204 / 255, 206 / 255, 205 / 255))
ax.bar(left=x1, height=y2, width=np.pi / 5, color='w', edgecolor=(204 / 255, 206 / 255, 205 / 255))

random.seed(100)
y4 = [random.randint(4000, 5500) for i in range(10)]
y5 = [random.randint(3000, 5000) for i in range(10)]

ax.bar(left=x2, height=y4, width=np.pi / 10, color=(206 / 255, 32 / 255, 69 / 255),
       edgecolor=(206 / 255, 32 / 255, 69 / 255))
ax.bar(left=x3, height=y5, width=np.pi / 10, color=(34 / 255, 66 / 255, 123 / 255),
       edgecolor=(34 / 255, 66 / 255, 123 / 255))

y6 = [2000 for i in range(0, 10)]
ax.bar(left=x1, height=y6, width=np.pi / 5, color='w', edgecolor='w')

plt.show()
