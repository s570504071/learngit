#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as bs
def getpage(url):
    res=urllib2.urlopen(url)
    r=res.read()
    soup=bs(r,'html.parser')
    naruto=soup.find_all('a',class_='j_th_tit')
    for i in naruto:
        print i.string
def main():
    url='https://tieba.baidu.com/f?ie=utf-8&kw=%E7%81%AB%E5%BD%B1%E5%BF%8D%E8%80%85'
    f=getpage(url)
main()
