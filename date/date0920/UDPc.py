#coding=utf-8
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in ['M','T','L']:
    s.sendto(data,('127.0.0.1',9999))#发送
    print s.recv(1024)#接收
s.close()#客户端要关闭
