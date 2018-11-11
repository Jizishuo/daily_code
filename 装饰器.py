

def aa(a):
    def bb(b):
        print (a+b)
        return aa
    return bb

q = aa(5)

w = q(4)

#w




def set_func(func):
    print("开始装饰1111")
    def call_func(*args, **kwargs):
        print("xxxxxx")
        print('11111')
        return func(*args, **kwargs)
    return call_func


def set_func2(func):
    print("开始装饰2222")
    def call_func(*args, **kwargs):
        print("xxxxxx")
        print('22222')
        return func(*args, **kwargs)
    return call_func

import functools

def set_func3(func):
    print("开始装饰3333")

    @functools.wraps(func)  # 内层函数属性变得跟被装饰的函数一样
    def call_func(*args, **kwargs):
        print("xxxxxx")
        print('3333')
        return func(*args, **kwargs)
    return call_func


@set_func
@set_func2   #test = set_func(test)
@set_func3
def text(num, *args, **kwargs):
    print("text---%s" %  num)
    return 'ok'

ret = text(100)
print(ret)
#开始装饰
#xxxxxx
#66666
#text---100
#ok


#有参数的装饰器
def fun1(pre = ''):
    #装饰器再加一层
    def fun2(func):
        def fun3():
            print("xxx")
            return func() #foo
        return fun3

    return fun2

@fun1('xxxx')
def foo():
    print("foo")


#类装饰器
class TTT(object):
    def __init__(self, func):
        print("init")
        self.__func = func

    def __call__(self, *args, **kwargs):
        print("call") #装饰器功能
        self.__func()
@TTT
def lalalll():
    print('lallalalal')

T = lalalll()


def lalal():
    i = 0
    while i< 5:
        if i ==0:
            ten = yield i
        else:
            yield i
        i+=1
t = lalal()
t.__next__()
t.send('999')



#多任务--携程
def ttt1():
    while True:
        print('11')
        yield None

def ttt2():
    while True:
        print("222")
        yield None

t1 = ttt1()
t2 = ttt2()
while True:
    #相当于同时执行t1.t2
    t1.__next__()
    t2.__next__()