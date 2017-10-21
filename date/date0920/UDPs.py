#coding=utf-8
import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
print 'UDP to 9999'
while True:
    data,addr=s.recvfrom(1024)
    print '%s:%s'%addr
    s.sendto('Hi,%s'%data,addr)
#先运行该程序，才能运行UDPs
