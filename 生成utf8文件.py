'''
f = open(r'./1.txt', 'w')
f.write(u'中文:你好')
f.close()
'''

import codecs

f = codecs.open(r'./1.txt', 'w', encoding='utf-8')
f.write(u'这个才是utf-8')
f.close()


