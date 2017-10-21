#-*-coding:utf-8-*-
import requests
res=requests.get('http://www.dilidili.wang')
#转码部分
res.raise_for_status()
res.encoding=res.apparent_encoding
res_code=res.status_code
#以上转码部分
print res_code
print res.headers['content-length']
print res.text