#coding=utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.baidu.com',80))
s.send('GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
d=[]
while True:
    data=s.recv(1024)
    if data:
        d.append(data)
    else:
        break
html=''.join(d)
s.close()
header,htm=html.split('\r\n\r\n',1)
print header
with open('bai.html','wb') as f:
    f.write(htm)
