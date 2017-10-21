#coding=utf-8
import urllib
import urllib2
import re
from bs4 import BeautifulSoup as bs
class GetL(object):
    def __init__(self):
        self.user_agent='Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.header={'User-Agent':self.user_agent}
        self.blue_link=''
    def getlink(self,link):
        #伪装，发送请求
        req=urllib2.Request(link,headers=self.header)
        res=urllib2.urlopen(req)
        html=res.read().decode('utf-8')
        soup=bs(html,'html.parser')
        content=soup.select('div.entry-content')
            #正则表达式匹配
        pattern=re.compile(r'([a-z0-9A-Z]{40}|[a-z0-9本站不提供下载A-Z]{54})</')
        blue_link1=pattern.findall(str(content))
        print content
if __name__=='__main__':
    #main()
    #main0()
    link='http://www.hacg.at/wp/all/anime/%e5%83%95%e3%81%a0%e3%81%91%e3%81%ae%e3%83%98%e3%83%b3%e3%82%bf%e3%82%a4%e3%82%ab%e3%83%8e%e3%82%b8%e3%83%a7-%e3%82%82%e3%81%a3%e3%81%a8-the-animation/'
    k=GetL()
    k.getlink(link)
#网页写错
