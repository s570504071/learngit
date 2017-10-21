class Cj:
    
    def __init__(self,score):
        self.score=score
        if score in range(90,101):
            print 'classA'
    
        elif score in range(80,91):
            print 'classB'
    
        elif score in range(70,81):
            print 'classC'
    
        elif score in range(60,71):
            print 'classD'
    
        elif score in range(0,61):
            print 'classF'
        elif score not in range(0,101):
            print 'please enter a number 0-100'

'''
def class1(self,score):
        if score in range(90,101):
            print 'classA'
    
        elif score in range(80,91):
            print 'classB'
    
        elif score in range(70,81):
            print 'classC'
    
        elif score in range(60,71):
            print 'classD'
    
        elif score in range(0,61):
            print 'classF'
            '''
        
        
