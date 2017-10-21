class Addgoods(object):
    def add_goods(self):
        global total
        total={}
        standard=True
        num=0
        total_price=[]
        while standard:
            goods=raw_input('What do you need?enter==>')
            num=0
            if goods=='q':
                standard=False
            else:
                price=raw_input('goods" price==>')
                total[goods]=price
                print total
                total_price.append(int(price))
                for n in total_price:
                    num+=n
                print 'all money:',num
class Delgoods(Addgoods):
    def del_goods(self):
        del_goods=raw_input('what do you want to del?enter==>')
        total_copy=total
        #del doesn't work!!!
        if del_goods in total_copy:
            del del_goods
        print total_copy    
if __name__=='__main__':
    need=Addgoods()
    need.add_goods()
    choice=raw_input('you choice:')
    if choice=='delete':
        delete=Delgoods()
        delete.del_goods()
