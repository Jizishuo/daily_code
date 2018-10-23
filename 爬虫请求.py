import urllib.request

def run_demo():
    f=urllib.request.urlopen('http://www.jizishuo.cn/')
    print(f.read())

if __name__=='__main__':
    run_demo()