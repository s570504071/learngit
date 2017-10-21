import sys,timer
reps=10000
repslist=range(reps)
#for循环
def forloop():
    res=[]
    for x in repslist:
        res.append(x+10)
    return res
#列表解析
def listcomp():
    return[x+10 for x in repslist]
#map调用
def mapcall():
    return map((lambda x:x+10),repslist)
#生成器表达式
def genexpr():
    return list(x+10 for x in repslist)
#生成器函数
def genfunc():
    def gen():
        for x in repslist:
            yield x+10
    return list(gen())
print sys.version
for test in (forloop,listcomp,mapcall,genexpr,genfunc):
    elapsed,result=timer.timer(test)
    print '-'*33
    print ('%-9s:%.5f => [%s...%s]'%
           (test.__name__,elapsed,result[0],result[-1]))
