fname=raw_input('Enter filename:')
print
try:
    fobj=open(r'D:/Python27/date0824/fname','r')
except IOError,e:
    print '*** file open error:',e
else:
    for eachline in fobj:
        print eachline,
    fobj.close()
