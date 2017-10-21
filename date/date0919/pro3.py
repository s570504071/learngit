#coding=utf-8
import time, threading
balance=0
lock=threading.Lock()
def change_it(n):
    global balance
    balance-=n
    balance+=n
def rn(n):
    print threading.current_thread().name
    for i in range(10):
        lock.acquire()
        try:
            change_it(n)
            print threading.current_thread().name
        finally:
            lock.release()
t1=threading.Thread(target=rn,args=(3,))
t2=threading.Thread(target=rn,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
print threading.current_thread().name
