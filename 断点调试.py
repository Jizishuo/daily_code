

def getAv(a, b):
    result = a+b
    print(result)
    return result

a = 100
b =200
c =a+b
ret = getAv(a, b)
print(ret)

#暂停 等输入
#python -m pdb xxx.py
# l list 看走到哪一步(全部代码)
# n next 走一波 (具体哪一行代码)
# c contiue 继续执行代码
# b break 添加断点 b 7 c 执行到第7行停 （可以多个断点）
# clear 1 删除第一个断点
# s ---step 在ret = getAv(a, b) 回进入函数
# p print 打印一个变量的值 p a 打印 100
# a args 打印所有形参的数据 a 打印 a=100, b=200
# q quit 退出调试
# r return 快速执行函数到最后一行
