class accesscontrol:
    def __setattr__(self,attr,value):
        if attr=='age':
            self.__dict__[attr]=value
        else:
            raise AttributeError,attr+' not allowed'
