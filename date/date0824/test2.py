import os
ls=os.linesep#ls='\r\n'
while True:
    if os.path.exists(r'D:/Python27/date0824/fname'):#be careful!change the filename
        print "ERROR:'%s' already exists"% fname
    else:
        break
all=[]
print "\nEnter lines('.' by itself to quit).\n"
while True:
    entry=raw_input('Please Start Here:')
    if entry=='.':
        break
    else:
        all.append(entry)
fobj=open(r'D:/Python27/date0824/fname','w')
fobj.writelines(['%s%s'%(x,ls)for x in all])
fobj.close()
print 'DONE!'
