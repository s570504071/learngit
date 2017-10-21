'''
Number 1,2,3,4,
get a three number that not repeat and different,
how many they are?

'''
class Num:
    def num1(self):
        a=[1,2,3,4]
        n=0
        for i in a:
            for j in a:
                if not i==j:
                    for k in a:
                        if not i==k and not j==k:
                            n+=1
                            number=i*100+j*10+k
                            print '%s => %s'%(n,number)
if __name__=='__main__':
    y=Num()
    y.num1()
