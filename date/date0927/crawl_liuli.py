#coding=utf-8
#琉璃神社首页   http://www.hacg.at/
#动漫页面   http://www.hacg.at/wp/category/all/anime/
import urllib2
import urllib
import json
import re
import logging
import pdb
from bs4 import BeautifulSoup as bs
class GetLink(object):
    def __init__(self):
        #self.url='http://www.hacg.at/wp/category/all/anime/'
        #self.num=num
        self.user_agent='Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.header={'User-Agent':self.user_agent}
        self.l=[]
        self.ani0={}
    def gethtml(self,u):
        self.ani={}
        #y=self.loop(num)
        #url_page=self.url+'page/'+str(self.num)+'/'
        req=urllib2.Request(u,headers=self.header)
        res=urllib2.urlopen(req)
        html=res.read().decode('utf-8')
        soup=bs(html,'html.parser')
        titles=soup.select('h1.entry-title > a')
        for title in titles:
            self.ani0[title.get_text()]=title.get('href')
            #用json格式输出汉字
            #print json.dumps(ani).decode("unicode-escape")
        return self.ani0
    #循环得到更多页的信息,(原先实际上只得到当前页的信息！！！）
    def loop(self,num):
        url='http://www.hacg.at/wp/category/all/anime/'
        for i in range(1,num):
            print 'downing--webpage---%s'%i
            url_page=url+'page/'+str(i)+'/'
            self.gethtml(url_page)
            self.ani.update(self.ani0)
        #print len(self.ani)
        return self.ani
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
        try:
            #正则表达式匹配
            pattern=re.compile(r'([a-z0-9A-Z]{40}|[a-z0-9本站不提供下载A-Z]{54})</')
            blue_link1=pattern.findall(str(content))
            #利用切片操作得到列表中的字符串或内容，可再次切片对字符串得到想要的
            blue_link0=blue_link1[0][:-2]
            self.blue_link=r'magnet:?xt=urn:btih:'+str(blue_link0)
        except Exception,e:
            print e
        finally:
            return self.blue_link
            #print self.blue_link 
    def findlink(self):
        #获得标题和网页链接
        l=GetLink()
        g=l.loop(3)
        print len(g)
        b_link={}
        for k,v in g.iteritems():
            print k
            #pdb.set_trace()
            self.getlink(v)
            b_link[k]=self.blue_link
        #print b_link
        print 'start'
        with open('b_link1.json','w') as f:
            f.write(str(b_link)+r'\n')
        print 'save down'
        return b_link
    
#获取所有最新信息        
def main():
    print '*'*8
    l=GetLink()
    g=l.loop(3)
    print g
    print '*'*8
#获取神秘代码
def main0():
    #link='http://www.hacg.at/wp/all/anime/%e3%83%92%e3%83%88%e3%83%85%e3%83%9e%e3%83%a9%e3%82%a4%e3%83%95-%e3%83%af%e3%83%b3%e3%82%bf%e3%82%a4%e3%83%a0%e3%82%ae%e3%83%a3%e3%83%ab-%e5%89%8d%e7%b7%a8/'
    #link='http://www.hacg.at/wp/all/anime/%e8%87%aa%e5%ae%85%e8%ad%a6%e5%82%99%e5%93%a1-3rd%e3%83%9f%e3%83%83%e3%82%b7%e3%83%a7%e3%83%b3-%e3%83%9b%e3%82%b7%e3%82%ac%e3%83%aa%e7%88%86%e4%b9%b3%e4%ba%ba%e5%a6%bb%e3%83%bb%e7%bf%94%e5%ad%90/'
    #link='http://www.hacg.at/wp/all/anime/%e5%83%95%e3%81%a0%e3%81%91%e3%81%ae%e3%83%98%e3%83%b3%e3%82%bf%e3%82%a4%e3%82%ab%e3%83%8e%e3%82%b8%e3%83%a7-%e3%82%82%e3%81%a3%e3%81%a8-the-animation/'
    k=GetL()
    k.findlink()
if __name__=='__main__':
    #main()
    main0()
