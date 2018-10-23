import urllib
#前半部分的链接(注意是http，不是https)
url_pre = "http://www.baidu.com/s"

params = {}
#GET参数
params['wb'] = u'测试'.encode('utf-8')
url_params = urllib.parse.urlencode(params)
#GET请求完整链接
url = '%s?%s' % (url_pre, url_params)
#打开链接，获取响应
response = urllib.request.urlopen(url)
#获取响应的html
html = response.read()
#将html保存到文件
'''with open('text.txt', 'x') as f:
    f.write(html)
'''

#POST请求
import urllib
'''
values = {}
values['usrname'] = 'aaa'
values['pwd'] = 'xxxx'
data = urllib.parse.urlencode(values)

url = 'http:xxxxx'
request = urllib.request.Request(url, data)

response = urllib.request.urlopen(request)
html = response.read()
print(html)
'''
#处理Cookie
import urllib
import http.cookiejar as ck

# 创建cookie
cookie = ck.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)

# 通过handler来构建自定义opener
opener = urllib.request.build_opener(handler)

# 此处的open方法同urllib2的urlopen方法
request = urllib.request.Request('http://www.baidu.com')
response = opener.open(request)
for item in cookie:
    print('%s = %s' % (item.name, item.value))

#cookie状态保持
import urllib
import http.cookiejar as ck

# 设置保存cookie的文件路径
filename = 'cookie.txt'

# 使用MozillaCookieJar创建cookie对象
cookie = ck.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)

# 通过handler来构建opener
opener = urllib.request.build_opener(handler)

# 创建请求，同urllib2的urlopen
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

# 设置header
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
# 构造Request请求，其中第二个参数是data
url = 'http://www.server.com/login'
request = urllib.request.Request(url, None, headers)