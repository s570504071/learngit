x=[1,3,4]
y='spam'
z=[12,35,675]
try:
    x+z
finally:
    print 'error'

print 'you success'


try:
    x+y
finally:
    print 'another error'
