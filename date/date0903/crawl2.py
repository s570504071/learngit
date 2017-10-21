#_*_coding:utf-8_*_
import urllib2
class Save(object):
    def save_html(self):
        req='http://www.baidu.com'
        response=urllib2.urlopen(req)
        html=response.read()
        f=open(r'D:\Python27\date0903\html.txt','w')
        f.write(html)
        f.close()
        print 'work done'
if __name__=='__main__':
    s=Save()
    s.save_html()
