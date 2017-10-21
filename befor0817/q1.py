p=1
c=2
z=3
def adder(good=23,*args):
    total=args[0]+good
    for arg in args[1:]:
        total=arg+total
    return total
