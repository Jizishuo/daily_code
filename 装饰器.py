
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


def set_func3(func):
    print("开始装饰3333")
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
