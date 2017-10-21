#coding=utf-8
import urllib
from htmlentitydefs import name2codepoint
from HTMLParser import HTMLParser
class M(HTMLParser):
    pass
parser=M()
k=parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')
print k
