#coding=utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print '---%s'%s.recv(1024)#对应‘---Welcome!’，其中recv是接收对方的信息
for data in ['M','L','T','PPP']:
    s.send(data)#有send才能通信
    print '***%s'%s.recv(1024)
s.send('exit')
s.close()
