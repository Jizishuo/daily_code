
'''
import threading

loop = int(1E7)

def _add(loop:int=1):
    global number
    for i in range(loop):
        number +=1

def _sub(loop:int=1):
    global number
    for i in range(loop):
        number -= 1

number = 0
ta = threading.Thread(target=_add, args=(loop,))
ts = threading.Thread(target=_sub, args=(loop,))
ta.start()
ts.start()
ta.join()
ts.join()
print(number) #这个 不一定是0
number = 0
ta = threading.Thread(target=_add, args=(loop,))
ts = threading.Thread(target=_sub, args=(loop,))
ta.start()
ta.join()

ts.start()
ts.join()
print(number) #这个 是0
'''

'''
# 父子进程
import os
ret = os.fork()

xx = 100  #全局变量
print(ret)
if ret > 0 :
    print("父进程 ---%s" % os.getpid()) #pid 进程最大6.5w
    xx +=1
    print(xx) #101 数据不共享
else:
    print("子进程---%s---%s" % (os.getpid(), os.getppid()))
    print(xx) #100
'''

'''
#多进程 start 开始 jion子进程等待父进程
from multiprocessing import Process
import time
import random

def ttxt():
    for i in range(random.randint(1, 5)):
        print('txt _-%s' % i)
        time.sleep(1)
p = Process(target=ttxt())

p.start() #开始执行txt的代码
p.join()  #堵塞 子进程执行完 才能继续 p.join(timeout) 等待几秒

#p.terminate() 直接杀死子进程

print("---main---")
'''

'''
#进程池
from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_s = time.time()
    print("%s开始执行 %s进程号" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_t = time.time()
    print('%s执行完毕 耗时%s' % (msg, t_t-t_s))


if __name__ == '__main__':
    po = Pool(3)  # 进程最大进程数 3个不同pid 使用
    for i in range(1, 10): #重复添加任务
        #(要调用的目标， （调用目标的参数）)
        po.apply_async(worker, (i,))#(i,)传进去的参数 非堵塞
        #po.apply(worker, (1,)) #堵塞方式

    print("strat")
    po.close()
    po.join()
    print('end')
'''

#进程间通信 队列queue
#from multiprocessing import Queue

#练习代码
'''
from multiprocessing import Pool, Manager
import os

def copyfile(name, oldname, newfile, queue):
    fr = open(oldname+"/"+name, 'r')
    fw = open(newfile+'/'+ name,'w')

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    oldname = input('请输入文件夹名字')

    newfile = oldname + '复件'

    os.mkdir(newfile)

    filenames = os.listdir(oldname)

    pool = Pool(5)
    queue = Manager().Queue()
    for name in filenames:
        pool.apply_async(copyfile, args=(name, oldname, newfile, queue))

    num = 0
    allnum = len(filenames)
    while num < allnum:
        queue.get()
        num += 1
        copyrate = num/allnum
        print("\rcopy进度%s %%" % (copyrate*100), end='')



if __name__ == '__main__':
    main()
'''


#线程
'''
from multiprocessing import Process
from threading import Thread
import time

def text():
    a = 0
    while True:
        a+=1
    #print("threaing")
    #time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        #t = Process(target=text)
        t = Thread(target=text)
        t.start()
'''

#线程变量共享问题 可能会乱
'''
from threading import Thread
import time

g_num = 100

def work1():
    global g_num
    for i in range(3):
        g_num += 1

    print('work1_%s' % g_num)

def work2():
    global g_num
    print('work2--%s' % g_num)

print("main--%s" % g_num)

t1 = Thread(target=work1)
t1.start()

time.sleep(1)

t2 = Thread(target=work2)
t2.start()
'''


#锁
'''
from threading import Thread, Lock
import time

g_num = 100

def work1():
    global g_num
    #2个进程抢上锁
    mutex.acquire() #上锁
    for i in range(3):
        g_num += 1
    mutex.release() #放锁
    print('work1_%s' % g_num)

def work2():
    global g_num
    mutex.acquire()  # 上锁
    for i in range(6):
        g_num +=1
    mutex.release()  # 放锁
    print('work2--%s' % g_num)

print("main--%s" % g_num)
mutex = Lock() #实例化锁  互测锁

t1 = Thread(target=work1)
t1.start()

#time.sleep(1)

t2 = Thread(target=work2)
t2.start()
'''


#异步
'''
from multiprocessing import Pool
import time
import os

def text():
    print("进程--pid:%s ppid%d" % (os.getpid(), os.getppid()))
    for i in range(3):
        print(i)
        time.sleep(1)
    return '11111'

def text2(args):
    print("callback-pid:%s" % os.getpid())
    print('callback--%s' % args)

if __name__ == "__main__":
    pool = Pool(3)
    pool.apply_async(func=text, callback=text2)

    while True:
        time.sleep(1) #主进程 子进程异步
        print("main pid: %s" % os.getpid())
'''


#gil锁
#单线程死循环
#while True:
    #pass

#线程死循环
#import threading

#def tt():
    #while True:
#         pass
# t1 = threading.Thread(target=tt)
# t1.start()
# while True:
#     pass

#进程死循环
# import multiprocessing
#
# def xx():
#     while True
#         pass
# p1 = multiprocessing.Process(target=xx)
# p1.start()
# xx()


#携程
'''
import time

def A():
    while True:
        print("---a")
        yield
        time.sleep(0.5)

def B(c):
    while True:
        print('---b')
        c.next()
        time.sleep(0.5)

if __name__ == '__main__':
    a = A()
    B(a) #ab 任务不停切换
'''

#greenlet携程
'''
from greenlet import greenlet
import time

def A():
    while True:
        print("---a")
        gr2.switch()
        time.sleep(0.5)

def B():
    while True:
        print('---b')
        gr1.switch()
        time.sleep(0.5)

if __name__ == '__main__':
    gr1 = greenlet(A)
    gr2 = greenlet(B)

    gr1.switch() #开始
'''


#gevent 开携程
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

        gevent.sleep(1)  #模拟程序运行时间大,不用time

if __name__ == '__main__':
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)

    g1.join()
    g2.join()
    g3.join()