#coding=utf-8
import urllib
import urllib2
def geth(url):
    res=urllib2.urlopen(url)
    html=res.read()
    print html
if __name__=='__main__':
    url='http://daily.zhihu.com/'
    geth(url)
    
