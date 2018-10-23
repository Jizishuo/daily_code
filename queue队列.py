#基本FIFO队列 --先进先出
from queue import Queue
q = Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
    #01234

#LIFO队列 --后进先出
from queue import LifoQueue
q = LifoQueue()
for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
    #43210