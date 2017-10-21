#coding=utf-8
#琉璃神社首页   http://www.hacg.at/
#动漫页面   http://www.hacg.at/wp/category/all/anime/
import urllib2
import urllib
import json
import re
from bs4 import BeautifulSoup as bs
class GetLink(object):
    def __init__(self):
        #self.url='http://www.hacg.at/wp/category/all/anime/'
        #self.num=num
        self.user_agent='Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.header={'User-Agent':self.user_agent}
    def gethtml(self,u):
        ani={}
        #y=self.loop(num)
        #url_page=self.url+'page/'+str(self.num)+'/'
        req=urllib2.Request(u,headers=self.header)
        res=urllib2.urlopen(req)
        html=res.read().decode('utf-8')
        soup=bs(html,'html.parser')
        titles=soup.select('h1.entry-title > a')
        for title in titles:
            ani[title.get_text()]=title.get('href')
            #用json格式输出汉字
            print json.dumps(ani).decode("unicode-escape")
        #return ani
    #循环得到更多页的信息
    def loop(self,num):
        url='http://www.hacg.at/wp/category/all/anime/'
        for i in range(1,num):
            url_page=url+'page/'+str(i)+'/'
            self.gethtml(url_page)
class GetL(object):
    def __init__(self):
        self.user_agent='Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.header={'User-Agent':self.user_agent}
    def getlink(self,link):
        #伪装，发送请求
        req=urllib2.Request(link,headers=self.header)
        res=urllib2.urlopen(req)
        html=res.read().decode('utf-8')
        soup=bs(html,'html.parser')
        content=soup.select('div.entry-content')
        #正则表达式匹配
        pattern=re.compile(r'[a-z0-9]{40}</')
        blue_link1=pattern.findall(str(content))
        #利用切片操作得到列表中的字符串或内容，可再次切片对字符串得到想要的
        blue_link0=blue_link1[0][:-2]
        blue_link=r'magnet:?xt=urn:btih:'+str(blue_link0)
        print blue_link
    def findlink(self,name):
        b_link={}
        for k,v in ani.iteritems():
            self.getlink(v)
            blink[k]=bluelink
        print b_link
#获取所有最新信息        
def main():
    print '*'*8
    l=GetLink()
    l.loop(2)
    print '*'*8
#获取神秘代码
def main0():
    #link='http://www.hacg.at/wp/all/anime/%e3%83%92%e3%83%88%e3%83%85%e3%83%9e%e3%83%a9%e3%82%a4%e3%83%95-%e3%83%af%e3%83%b3%e3%82%bf%e3%82%a4%e3%83%a0%e3%82%ae%e3%83%a3%e3%83%ab-%e5%89%8d%e7%b7%a8/'
    link='http://www.hacg.at/wp/all/anime/%e8%87%aa%e5%ae%85%e8%ad%a6%e5%82%99%e5%93%a1-3rd%e3%83%9f%e3%83%83%e3%82%b7%e3%83%a7%e3%83%b3-%e3%83%9b%e3%82%b7%e3%82%ac%e3%83%aa%e7%88%86%e4%b9%b3%e4%ba%ba%e5%a6%bb%e3%83%bb%e7%bf%94%e5%ad%90/'
    k=GetL()
    k.getlink(link)
if __name__=='__main__':
    #main()
    main0()
