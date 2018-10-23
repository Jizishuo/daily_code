a = globals()
b =a['__builtins__'].__dict__
c = b['print']('aaaaaaa')
print(c)

#动态类
type('AAA', (), {'num ':1, 'num2':2})
