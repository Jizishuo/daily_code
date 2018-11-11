a = globals()
b =a['__builtins__'].__dict__
c = b['print']('aaaaaaa')
print(c)

#动态类 类名称，继承谁， 参数(定义属性和方法)
type('AAA', (), {'num ':1, 'num2':2})

import gc
#无限占用内存
class Ccc():
    def __init__(self):
        print("222")

def f2():
    while True:
        c1 = Ccc()
        c2 = Ccc()

        c1.t = c2
        c2.t = c1

        del c1
        del c2

gc.disable() #关闭隔代回收
f2()


class Itcast(object):
    def __init__(self, sub):
        self.sub = sub
        self.sub2 = 'cpp'

    #访问属性拦截 ，打印log
    def __getattribute__(self, item):
        if item == "sub":
            print("sublalalalal")
            return 'redirect python'
        else:
            return object.__getattribute__(self, item)

    def show(self):
        print('iaiaiaiai')

s = Itcast('py')
print(s.sub)
print(s.sub2)


#bug
class Itcast2(object):

    #访问属性拦截 ，打印log
    def __getattribute__(self, item):
        if item.startswith('a'):
            print("sublalalalal")
            return 'redirect python'
        else:
            return self.show() #w问题在这里

    def show(self):
        print('iaiaiaiai')

s = Itcast2()
print(s.a)
print(s.b)#这里会死掉



#偏函数
import functools

def showarg(*args, **kw):
    print(args)
    print(kw)

p1 = functools.partial(showarg, 1,2,3)
p1()  #123
p1(4,5,6) # 123456

#只需要传一次就不需要再传 参数累加
