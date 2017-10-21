#-*-coding:utf-8-*-
#斐波那契数列
l=[0,1]
for i in range(10):
    p=reduce(lambda x,y:x+y,(l[-1],l[-2]))
    l.append(p)
print 'l:{0}'.format(l)
#map函数
v=map(lambda x:x+2,[1,2,3,4,5])
print 'v:{0}'.format(v)
p1=map(lambda x,y:x+y,[1,2,3,4],[3,423,4,32])
print 'p1:{0}'.format(p1)
#reduce函数
p2=reduce(lambda x,y:x+y,[1,2,3,4])
print 'p2:{0}'.format(p2)