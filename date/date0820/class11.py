class Callee:
    def __call__(self,*pargs,**kargs):
        print 'Called:',pargs,kargs
        
c=Callee()
c(1,2,3)
class c:
    def __call__(self,a,b,c=5,d=6):
        print a,b,c,d
x=c()
x(1,2)
x(1,2,3,4)
class c:
    def __call__(self,*pargs,**kargs):
        print pargs,kargs
x=c()
x(a=1,b=2,d=4)
x(*[1,2],**dict(c=3,d=4))
'''
python 3.0
class c:
    def __call__(self,*pargs,d=6,**kargs):
        print pargs,d,kargs
x(1,*(2),c=3,**dict(d=4))
'''
