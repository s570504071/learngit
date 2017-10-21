#coding=utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.qq.com',80))
s.send('GET / HTTP/1.1\r\nHost: www.qq.com\r\nConnection: close\r\n\r\n')
b=[]
while True:
    d=s.recv(1024)
    if d:
        b.append(d)
    else:
        break
data=''.join(b)
s.close()
header,html=data.split('\r\n\r\n',1)
print header
#print html
with open('qq.html','wb') as f:
    f.write(html)
