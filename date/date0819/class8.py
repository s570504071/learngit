class Indexer:
    def __getitem__(self,index):
	return index**2
x=Indexer()
x[2]
x.__getitem__(15)
