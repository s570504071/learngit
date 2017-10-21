class stepper:
    def __getitem__(self,i):
        return self.data[i]
x=stepper()
x.data='spam'
x[1]
for item in x:
    print item
