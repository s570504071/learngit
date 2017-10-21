#coding=utf-8
import urllib
import urllib2
from bs4 import BeautifulSoup as bs
#from urllib2 import Request#this is useful in 2.7
#form urllib2 import request#this is unuseful in 2.7 but 3.5 


class GetPage(object):
    def __init__(self):
        pass
    def GetUrl(self):
        url=raw_input('enter your url:')#https://movie.douban.com/nowplaying/hangzhou/
        #use urllib2.urlopen!!!not urllib.urlopen
        res=urllib.urlopen(url)
        global r#simple but use!
        r=res.read()
        #if not return r,it seems return None
        return r
    #it is too comlepx to save a file easily
    def Save(self):
        #G=self.GetUrl(),this is not need
        f=open(r'D:/Python27/date0909/movie.txt','w')
        f.write(r)
        f.close()
class GetMovieId(GetPage):
    def movie_id(self):
        soup=bs(r,'html.parser')
        div_id=soup.find_all('div',id="nowplaying")
        div_id_list=div_id[0].find_all('li',class_='list-item')#can't use class direct
        id_list=[]
        for i in div_id_list:
            id_dict={}
            id_dict['id']=i['id']#also can use data-subject
            for name in i.find_all('img'):
                id_dict['name']=name['alt']
                id_list.append(id_dict)
        return id_list
        #print id_list
class GetComment(GetPage):
    def comment(self,movieid):
        urlc='https://movie.douban.com/subject/'+movieid+'/comments'+'?' +'start=0' + '&limit=20'
        #urlc='https://movie.douban.com/subject/'+movieid+'/comments'+'?' +'status=P'
        resc=urllib2.urlopen(urlc)
        c=resc.read()
        soupc=bs(c,'html.parser')
        c_div=soupc.find_all('div',class_='comment')
        #print c_div
        comment_list=[]
        for i in c_div:
            print type(i.find_all('p')[0])
            #print i.find_all('p')[0].string#find in bs4,you must be understand it,chinese!!!
            comment_list.append(i.find_all('p')[0].string)
        #print comment_list #unicode,not chinese
        return comment_list
def main():
    k=GetPage()
    k.GetUrl()
    k.Save()
    print 'done'
    g=GetMovieId()
    g.movie_id()
    p=GetComment()
    p.comment(g.movie_id()[1]['id'])#change the number can select different movie!
    #print g.movie_id()[1]['name']
    print 'ok'
main()
'''
problem1:how to use the class but different def???
answer:global!not best but use

problem2:when and where use urllib or urllib2?
answer:urllib2.urlopen

problem3:how to use a parameter when you need to use it in def?
ansewer:pass parameter to a def when you need to use it in def

problem4:why show 'not __getitem__'?
answer:remeber use return!!! 

note:to use .read(),otherwise you can't read the content
'''
