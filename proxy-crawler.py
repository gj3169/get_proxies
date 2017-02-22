# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 10:55:40 2017

@author: gj3169
"""
import socks
import socket
import requests
from bs4 import BeautifulSoup

def proxies():
    socks.set_default_proxy(socks.SOCKS5, "localhost", 60002)
    socket.socket = socks.socksocket
    
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
    url = 'http://cn-proxy.com/'
    html_1 = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_1.text, 'lxml')
    proxies = []
    for a in soup.body.findAll('tbody'):
        for b in a.findAll('tr'):
            proxies.append(b.td.text+':'+b.td.nextSibling.nextSibling.text)
    return proxies
