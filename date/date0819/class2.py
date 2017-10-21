class Super:
    def __init__(self,x):
        print 'attention please: in Super.method'
class Sub(Super):
    def __init__(self,x,y):
        print 'starting Sub.method'
        Super.__init__(self,x)
        print 'ending Sub.method'
p=Super(667)
i=Sub(2,6)
