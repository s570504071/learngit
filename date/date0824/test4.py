def displayNumType(num):
    print num,'is',
    if type(num)==type(0):
        print 'an interger'
    elif type(num)==type(0L):
        print 'a long'
    elif type(num)==type(0.0):
        print 'a float'
    elif type(num)==type(0+0j):
        print 'a complex number'
    else:
        print 'not a number at all!'
