class Printer:
    def __init__(self,val):
        self.val=val
#   def __str__(self):  this is not as good as __repr__
    def __repr__(self):
        return str(self.val)#here str intend to change the type of self.val

objs=[Printer(2),Printer(3)]
for x in objs:print x
print objs
objs
