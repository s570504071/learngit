import thread
from time import sleep,ctime 
def fun1():
    print '1 start:',ctime()
    sleep(3)
    print '1 done:',ctime()
def fun2():
    print '2 start:',ctime()
    sleep(5)
    print '2 done:',ctime()
if __name__=='__main__':
    print 'starting:',ctime()
    thread.start_new_thread(fun1,())
    thread.start_new_thread(fun2,())
    sleep(10)
    print 'Done:',ctime()
