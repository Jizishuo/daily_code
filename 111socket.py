import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8000))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    conn.recv(1024) #收消息
    conn.send(b'HTTP/1/1 200 OK\r\n\r\n<h1>666666<h1>')
    #conn.send(b'666666') #发消息
    #with open('data.txt', 'rb') as f: #data.html
        #msg = f.read()
    # conn.send(msg) #发消息
    conn.close()
