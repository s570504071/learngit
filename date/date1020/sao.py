#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup as bs
def sao(url,header):
    res=requests.get(url,headers=header)
    res.raise_for_status()
    res.encoding=res.apparent_encoding
    res=res.text
    #print res.text
    soup=bs(res,'html.parser')
    content=soup.find_all('div',class_="d_post_content j_d_post_content ")
    for n,con in enumerate(content):
        #print '{0}:{1}'.format(n,con)
        print '{0}:{1}'.format(n, str([c for c in con.children]))
if __name__=='__main__':
    url = 'https://tieba.baidu.com/p/5050282361?see_lz=1'
    user_agent = 'Mozilla/5.0 (Window NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    header = {'User-Agent': user_agent}
    sao(url,header)