class Adder:
    def add(self,x,y):
        print 'Not Implemented'
    def __init__(self,start=[]):
        self.data=start
    def __add__(self,other):
        return self.add(self.data,other)
class ListAdder(Adder):
    def add(self,x,y):
        return x+y
class DictAdder(Adder):
    def add(self,x,y):
        new={}
        for k in x:new[k]=x[k]
        for k in y:new[k]=y[k]
        return new
    
