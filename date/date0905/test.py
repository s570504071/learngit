#_*_coding:utf-8_*_
__author__ = 'hang'
 
import warnings
warnings.filterwarnings("ignore")
import jieba    #分词包
import codecs   #codecs提供的open方法来指定打开的文件的语言编码，它会在读取的时候自动转换为内部unicode 
import re
import urllib
import json
from bs4 import BeautifulSoup as bs
resp = urllib.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
nowplaying_list = [] 
for item in nowplaying_movie_list:        
    nowplaying_dict = {}        
    nowplaying_dict['id'] = item['data-subject']       
    for tag_img_item in item.find_all('img'):            
        nowplaying_dict['name'] = tag_img_item['alt']           
        nowplaying_list.append(nowplaying_dict)
####good!!!but for dict just!!!
print json.dumps(nowplaying_list).decode("unicode-escape")
