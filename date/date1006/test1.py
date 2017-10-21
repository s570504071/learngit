#coding=utf-8
'''
s(n)=1    #n of number
s(n-1)=5*s(n)+1  and s     #n-1
s(n-2)=5(n-1)+1     #n-2
----------------------
s(n)
s(n)=5*s(n-1)+1
s(n)-s(n-1)-1=4*s(n-1)
s(n+1)=5*s(n)+1
------------------------
************************
s(first)=all_orange
s(second)=(s(first)-1)/5)*4
so---f(more)=5*s(less)/4+1
assum s(less)=s
because type(s(per number)) is int
so s(per number)%4==0!!!
question:where to end or begin?
answer:s(from 1 to monkey_number),s(monkey_number)=4*x,but x is what?if s(per number)%4==0: x=x+1
there are some problems to find!!!
'''
print '猴子问题'