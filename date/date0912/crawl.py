# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import traceback
import re
 
def getHTMLText(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text
 
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a',class_='bets-name')
    for i in a:
        href = i.attrs['href']
        lst.append(re.findall(r"[s][hz]\d{6}", href))

def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        if html=="":
            continue
        infoDict = {}
        soup = BeautifulSoup(html, 'html.parser')
        stockInfo = soup.find('div',attrs={'class':'stock-bets'})
 
        name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
        infoDict.update({'股票名称': name.text.split()[0]})
             
        keyList = stockInfo.find_all('dt')
        valueList = stockInfo.find_all('dd')
        for i in range(len(keyList)):
            key = keyList[i].text
            val = valueList[i].text
            infoDict[key] = val
             
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write( str(infoDict) + '\n' )
            count = count + 1
            print "\r当前进度: {:.2f}%".format(count*100/len(lst))
def main():
    print 'start'
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = r'D:\Python27\date0912\stock.txt'
    slist=[]
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
    print 'done'
main()
