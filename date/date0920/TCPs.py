#coding=utf-8
import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print 'waiting'
def tcplink(sock,addr):
    print 'Accept %s:%s'%addr
    sock.send('Welcome!')
    while True:
        data=sock.recv(1024)
        time.sleep(1)
        if data=='exit' or not data:
            break
        sock.send('Hi,%s'%data)
    sock.close()
    print '%s:%s end'%addr
while True:
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
#先运行soc2，再运行soc3