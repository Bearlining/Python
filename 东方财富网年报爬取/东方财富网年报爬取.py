#!/usr/bin/env python
# coding: utf-8

# # 东方财富网年报爬取

# In[2]:


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


# In[18]:


import requests,json
from bs4 import BeautifulSoup
import random
import pandas as pd
import re
import os
import shutil
import pandas as pd
import time


# In[19]:


dd = pd.read_excel('股票代码.xlsx',dtype=object)
all_id = dd['股票代码'].tolist()


# In[20]:


base_url = 'https://pdf.dfcfw.com/pdf/H2_'
for p in all_id:
    folder = 'E:/'+p
    os.mkdir(folder)
    for j in range(1,50):
        url = 'http://data.eastmoney.com/notices/getdata.ashx?StockCode='+p+'&CodeType=A&PageIndex=%d&PageSize=50&jsObj=lChcLpUT&SecNodeType=0&FirstNodeType=1&rt=53572523' %(j)
        html=requests.get(url,headers={'User-Agent':random.choice(USER_AGENT)},proxies=random.choice(IPS)) # 设置随机ip代理放反爬
        soup=BeautifulSoup(html.text,'html.parser')
        pat1 = '"art_code":"AN\w*","title":"\S{0,10}\s*\S{0,10}(\w{4}年年度报告)",'  # 防止错位，限定10，防止空格，加\s*
        pat2 = '"art_code":"(AN\w*)","title":"\S{0,10}\s*\S{0,10}\w{4}年年度报告",'
        pat3 = '"art_code":"AN\w*","title":"\S{0,10}\s*\S{0,10}(\w{4}年年报)",'
        pat4 = '"art_code":"(AN\w*)","title":"\S{0,10}\s*\S{0,10}\w{4}年年报",'
        title = re.compile(pat1).findall(soup.text)
        data_code = re.compile(pat2).findall(soup.text)
        title = title + re.compile(pat3).findall(soup.text)
        data_code = data_code + re.compile(pat4).findall(soup.text)
        for i in range(len(title)):
            pdf_url = base_url+data_code[i]+'_1.pdf' # 下载链接
            r = requests.get(pdf_url)
            file_name = folder+'/'+title[i]+'.pdf'
            fo = open(file_name,'wb')                         # 注意要用'wb',b表示二进制，不要用'w'
            fo.write(r.content)                               # r.content -> requests中的二进制响应内容：以字节的方式访问请求响应体，对于非文本请求
            fo.close()
            time.sleep(2)

