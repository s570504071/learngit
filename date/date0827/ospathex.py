import os
'''
for tmpdir in (r'D:\Python27\date0827'):
    #here exist a problem
    if os.path.isdir(tmpdir):
        break
    else:
        print 'no!!!'
        tmpdir=''
'''
#i read it myself!
tmpdir=r'D:\Python27\date0827'
if tmpdir:
    os.chdir(tmpdir)
cwd=os.getcwd()
print '*** current'
print cwd
print '*** creating...'
os.mkdir('example')
os.chdir('example')
cwd=os.getcwd()
print '*** new:'
print cwd
print '*** original:'
print os.listdir(cwd)
print '*** creating...'
fobj=open('test','w')
fobj.write('111\n')
fobj.write('222\n')
fobj.close()
print '*** updated:'
print os.listdir(cwd)
print "*** renaming 'test' to 'filetest.txt'"
os.rename('test','filename.txt')
print '*** updated:'
print os.listdir(cwd)
path=os.path.join(cwd,os.listdir(cwd)[0])
print '*** full'
print path
print '*** (pathname,basename)=='
print os.path.split(path)
print '*** (filename,extension)=='
print os.path.splitext(os.path.basename(path))
print '*** displaying'
fobj=open(path)
for eachLine in fobj:
    print eachLine,
fobj.close()
'''
print '***del'
os.remove(path)
print '***updated:'
print os.listdir(cwd)
os.chdir(os.pardir)
print '***del'
os.rmdir('example')
print '***DONE'
'''
