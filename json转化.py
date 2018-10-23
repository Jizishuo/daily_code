import json

text_dict = {'a':1, 'b':2}

#字典转json字符串
json_text = json.dumps(text_dict)
print(json_text)

#json字符串转字典
json_dict = json.loads(json_text)
print(json_dict)

import codecs
#把json字符串保存到文件
#因为可能json有unicode编码，最好用codecs保存utf-8文件
with codecs.open('1.json', 'w', 'utf-8') as f:
    f.write(json_text)

# 从文件中读取内容
with codecs.open('1.json', 'r', 'utf-8') as f:
    json_text = f.read()

# 把字符串转成字典
json_dict = json.loads(json_text)


#dump把字典转成json字符串并写入到文件
import json
import codecs

test_dict = {'a': 1, 'b': 2}

# 把字典转成json字符串并写入到文件
with codecs.open('1.json', 'w', 'utf-8') as f:
    json.dump(test_dict, f)

#load从json文件读取json字符串到字典
import json
import codecs

# 从json文件读取json字符串到字典
with codecs.open('1.json', 'r', 'utf-8') as f:
    json_dict1 = json.load(f)


#如何把json转成有序的字典。
from collections import OrderedDict
import json

json_text = '{ "b": 3, "a": 2, "c": 1}'

json_dict2 = json.loads(json_text)
print(u"转成普通字典")
for key, value in json_dict2.items():
    print("key:%s, value:%s" % (key, value))

json_dict = json.loads(json_text, object_pairs_hook=OrderedDict)
print(u"\n转成有序字典")
for key, value in json_dict.items():
    print("key:%s, value:%s" % (key, value))