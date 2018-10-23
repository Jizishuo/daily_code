s = sum(i*i for i in range(10))

xx = [1,2,3]
yy = [4,5,6]
b = sum(x*y for x, y in zip(xx,yy))

from math import pi, sin
sine ={x: sin(x*pi/180) for x in range(0, 91)}

unique_words = set(word  for line in 'page'  for word in line.split())
print(unique_words)

valedictorian = max((student.gpa, student.name) for student in graduates)

data = 'golf'
list(data[i] for i in range(len(data)-1, -1, -1))