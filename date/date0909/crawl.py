#coding=utf-8
import urllib
import urllib2


class GetPage(object):
    def GetUrl(self):
        url=raw_input('enter your url:')
        #use urllib2.urlopen!!!not urllib.urlopen
        res=urllib.urlopen(url)
        global r#simple but use!
        self.r=res.read()
        #if not return r,it seems return None
        return self.r
    #it is too comlepx to save a file easily
    def Save(self):
        #G=self.GetUrl(),this is not need
        f=open(r'D:/Python27/date0909/bili.htm','w')
        f.write(self.r)
        f.close()
def main():
    k=GetPage()
    k.GetUrl()
    k.Save()
    print 'done'
main()
'''
problem1:how to use the class but different def???
answer:global!not best but use

problem2:when and where use urllib or urllib2?
answer:urllib2.urlopen

problem3:how to save different url to different file?
answer:to be think

note:to use .read(),otherwise you can't read the content
'''
