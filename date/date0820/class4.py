class Iters:
    def __init__(self,value):
        self.data=value
    def __getitem__(self,i):
        print 'get[%s]:'% i
        return self.data[i]
        '''
    def __iter__(self):
        print 'iter=>'
        self.ix=0
        return self
'''
    def next(self):
        print 'next:'
        if self.ix==len(self.data):raise StopIteration
        item=self.data[self.ix]
        self.ix+=1
        return item
'''
    def __contains__(self,x):
        print 'contains:'
        return x in self.data
    '''
x=Iters([1,2,3,4,5])
print (3 in x)
for i in x:
    print i
print ()
print [i**2 for i in x]
print list(map(bin,x))
I=iter(x)
while True:
    try:
        print next(I)
    except StopIteration:
        break
    
