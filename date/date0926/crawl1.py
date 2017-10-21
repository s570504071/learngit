#coding=utf-8
import urllib
import urllib2
import MySQLdb
class getP(object):
    def __init__(self,url):
        self.user_agent='Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        self.headers={'User-Agent':self.user_agent}
        self.url=url
    def gethtml(self):
        req=urllib2.Request(self.url,headers=self.headers)
        res=urllib2.urlopen(req,timeout=10)
        html=res.read()
        print html
def main():
    url='http://www.baidu.com'
    p=getP(url)
    p.gethtml()
if __name__=='__main__':
    print 'start'
    main()
    print 'done'
