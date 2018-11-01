l1 = [2,3,4,5]
l2 = [1,3,4,6]


def add(num1, num2):
    return num1 + num2

def add_self(n):
    return n +2

a = map(add, l1, l2)

#print(a) py2--列表
print(list(a)) #py3--返回对象 需要加list转化
