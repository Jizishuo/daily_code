#__new__是新方法
#__init__是初始化方法

class A(object):
    def __init__(self):
        print('init')

    def __new__(cls, *args, **kwargs):
        print('new %s' % cls)
        return object.__new__(cls, *args, **kwargs)

# 实例化测试
a = A()
#输出
#new <class '__main__.A'>
#init


class A(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 判断__instance是否有None
        if cls.__instance is None:
            # 若为None，则new一个对象写入到该变量
            cls.__instance = object.__new__(cls, *args, **kwargs)

        # 返回该变量中的对象
        return cls.__instance

a = A()
a.value = 2
b = A()

print(b.value)
print(a is b)
print(a)
print(b)
#2
#True
#<__main__.A object at 0x024959F0>
#<__main__.A object at 0x024959F0>



class A(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        # 判断__instance是否有None
        if cls.__instance is None:
            # 若为None，则new一个对象写入到该变量
            cls.__instance = object.__new__(cls, *args, **kwargs)

        # 返回该变量中的对象
        return cls.__instance

    def __init__(self):
        self.value = 1

a = A()
a.value = 2  # 修改value属性为2
b = A()  # 再次获取实例
print(b.value)
#输出1