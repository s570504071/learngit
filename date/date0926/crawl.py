#coding=utf-8
import urllib
import urllib2
import MySQLdb
def gethtml(url):
    print '***'
    res=urllib2.urlopen(url,timeout=10)
    html=res.read()
    print len(html)
    print html
def input_db(time,name,ip):
    conn=MySQLdb.connect(user='root',passwd='password',db='test',port=3306)
    cursor=conn.cursor()
    cursor.execute('create table ')
def main():
    url='http://www.bilibili.com'
    gethtml(url)
if __name__=='__main__':
    main()
