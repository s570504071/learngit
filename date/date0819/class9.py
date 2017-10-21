class Indexer:
    data=[5,6,7,8,9]
    def __getitem__(self,index):
        print 'getitem:',index
        return self.data[index]
y=Indexer()
y[1]
