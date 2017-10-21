filename=raw_input('Enter:')
f=open(filename,'r')
for eachLine in f:
    print eachLine,
f.close()
