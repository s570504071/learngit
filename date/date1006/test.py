#coding=utf-8
import copy
a=[1,2,['a','b'],3]
b=a
c=copy.copy(a)
d=copy.deepcopy(a)
a.append(453)
a[2].append('c')
print 'a:%s,b:%s,c:%s,d:%s'%(id(a),id(b),id(c),id(d))
print 'a:%s,b:%s,c:%s,d:%s'%(a,b,c,d)