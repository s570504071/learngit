import urllib2
class Save(object):
    def save_html(self):
        response=urllib2.urlopen('http://www.baidu.com/')
        html=response.read()
        return html
if __name__=='__main__':
    s=Save()
    s.save_html()
