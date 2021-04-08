#!/usr/bin/env python
# coding: utf-8

# In[1]:


#浏览器头部
USER_AGENT = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
    "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
    "UCWEB7.0.2.37/28/999",
    "NOKIA5700/ UCWEB7.0.2.37/28/999",
    "Openwave/ UCWEB7.0.2.37/28/999",
    "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
    # iPhone 6：
    "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

]
# 代理ip
IPS=[{'HTTPS': '106.75.226.36:808', 'HTTP': '61.135.217.7:80'},
 {'HTTPS': '106.75.164.15:3128', 'HTTP': '118.190.95.35:9001'},
 {'HTTPS': '101.204.70.51:808', 'HTTP': '124.235.181.175:80'},
 {'HTTPS': '110.73.44.89:8123', 'HTTP': '110.73.6.70:8123'},
 {'HTTPS': '182.88.179.108:8123', 'HTTP': '110.73.0.121:8123'},
 {'HTTPS': '106.75.164.15:3128', 'HTTP': '61.135.217.7:80'},
 {'HTTPS': '106.75.226.36:808', 'HTTP': '222.94.145.158:808'},
 {'HTTPS': '121.31.192.106:8123', 'HTTP': '118.190.95.35:9001'},
 {'HTTPS': '106.75.164.15:3128', 'HTTP': '124.235.181.175:80'}
 ]


# In[2]:


import requests,json
from bs4 import BeautifulSoup
import random
import pandas as pd
import re
import os
import shutil
import pandas as pd
import time


# In[3]:


dd = pd.DataFrame()
dd.to_excel('D:/公告.xlsx')


# In[4]:


share_code = []
name = []
title = []
data_url = []
for j in range(1,24):
    url = 'http://www.cninfo.com.cn/new/fulltextSearch/full?searchkey=%E5%88%86%E6%8B%86&sdate=&edate=&isfulltext=false&sortName=pubdate&sortType=desc&pageNum='+ str(j)
    html=requests.get(url,headers={'User-Agent':random.choice(USER_AGENT)},proxies=random.choice(IPS)) # 设置随机ip代理放反爬
    soup=BeautifulSoup(html.text,'html.parser')
    data = soup.text.replace(' ','')
    pat1 = '"secCode":"(\w{0,6})","secName":"\S{0,20}","orgId":"\S{0,30}","announcementId":"\w{0,15}","announcementTitle":"\S{0,150}","announcementTime":\w{0,15},"adjunctUrl":"finalpage/\w{4}-\w{2}-\w{2}/\S{0,50}","adjunctSize'
    pat2 = '"secCode":"\w{0,6}","secName":"(\S{0,20})","orgId":"\S{0,30}","announcementId":"\w{0,15}","announcementTitle":"\S{0,150}","announcementTime":\w{0,15},"adjunctUrl":"finalpage/\w{4}-\w{2}-\w{2}/\S{0,50}","adjunctSize'
    pat3 = '"secCode":"\w{0,6}","secName":"\S{0,20}","orgId":"\S{0,30}","announcementId":"\w{0,15}","announcementTitle":"(\S{0,150})","announcementTime":\w{0,15},"adjunctUrl":"finalpage/\w{4}-\w{2}-\w{2}/\S{0,50}","adjunctSize'
    pat4 = '"secCode":"\w{0,6}","secName":"\S{0,20}","orgId":"\S{0,30}","announcementId":"\w{0,15}","announcementTitle":"\S{0,150}","announcementTime":\w{0,15},"adjunctUrl":"(finalpage/\w{4}-\w{2}-\w{2}/\S{0,50})","adjunctSize'
    share_code = share_code + re.compile(pat1).findall(data)
    name = name + re.compile(pat2).findall(data)
    title = title +  re.compile(pat3).findall(data)
    data_url = data_url + re.compile(pat4).findall(data)
    time.sleep(1)
for i in range(len(title)):
    data_url[i] = 'http://static.cninfo.com.cn/'+data_url[i]
dd['股票代码'] = share_code
dd['股票简称'] = name
dd['公告名称'] = title
dd['下载链接'] = data_url


# In[ ]:


dd.to_excel('D:/公告.xlsx')


# In[9]:


dd.to_excel('公告下载链接汇总.xlsx')


# In[9]:


url = 'http://www.cninfo.com.cn/new/fulltextSearch/full?searchkey=%E5%88%86%E6%8B%86&sdate=&edate=&isfulltext=false&sortName=pubdate&sortType=desc&pageNum=2'
html=requests.get(url,headers={'User-Agent':random.choice(USER_AGENT)},proxies=random.choice(IPS)) # 设置随机ip代理放反爬
soup=BeautifulSoup(html.text,'html.parser')
data = soup.text.replace(' ','')
print(data)


# In[10]:


data = soup.text.replace(' ','')
print(data)


# In[5]:


dawe = "干特么的大伟冰峰马骝无限啊哈哈哈哈"
pat = '干特么的(\S{2})\S{2}(\S{2})\S*'
da =  re.compile(pat).findall(dawe)
print(da)


# In[14]:


print(len(share_code))


# In[15]:


print(len(name))


# In[16]:


print(len(title))


# In[17]:


print(len(data_url))


# In[18]:


dd['股票代码'] = share_code
dd['股票简称'] = name
dd['公告名称'] = title
dd['下载链接'] = data_url

