class adder:
    def __init__(self,value=0):
        self.data=value
    def __add__(self,other):
        self.data+=other


x=adder()
print x

print '*'*8




class addrepr(adder):
    #__repr__ for any typr
    def __repr__(self):
        return 'addrepr(%s)'% self.data
x=addrepr(2)
x+1
x
str(x),repr(x)


class addstr(adder):
    def __str__(self):
        return '[Value:%s]'% self.data
x=addstr(3)
x+1
x
print x
str(x),repr(x)
