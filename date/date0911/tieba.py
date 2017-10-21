#coding=utf-8
import urllib
import urllib2
import re
import json
from bs4 import BeautifulSoup as bs
def getpage(url):
    res=urllib2.urlopen(url)
    r=res.read()
    f=open(r'D:\Python27\date0911\naruto.txt','w')
    f.write(r)
    f.close()
    soup=bs(r,'html.parser')
    naruto=soup.find_all('a',class_='j_th_tit')
    author=str(soup.find_all('span',class_='tb_icon_author'))
    pattern=re.compile('title='+'"'+r'主题作者:'+'(.*?)'+'"')
    aut=re.findall(pattern,author)
    a_dict={}
    print len(naruto)
    print len(aut)
    
    for i in range(len(naruto[:])):
        for k in range(len(aut[:])):
            if i==k:
                a_dict[aut[k]]=naruto[i].string
    #print a_dict
    print(json.dumps(a_dict).decode("unicode-escape"))
def main():
    #url='https://tieba.baidu.com/f?ie=utf-8&kw=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85'
    url='https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A4%A9%E8%8D%89%E7%AD%B1'
    f=getpage(url)
main()
'''
1:
how to 1=>1;2=>2,...???
to be think
if i==j:
ok!!!

2:
print(json.dumps(a_dict).decode("unicode-escape"))
this is to change dict to chinese

3:



'''
