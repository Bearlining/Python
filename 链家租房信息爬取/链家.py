# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:15:41 2021

@author: Bearlining
"""


import requests
from bs4 import BeautifulSoup
import re
import time
import pandas as pd

区域 = []
标题 = []
面积 = []
楼层 = []
总楼层 = []
价格 = []
小区信息 = []

class LJ:
    def __init__(self):
         self.headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36'}
         self.url = 'https://xm.lianjia.com/zufang'
        
        # 获取某市区域的所有链接
    def get_areas(self):
        print('start grabing areas')
        resposne = requests.get(self.url, headers=self.headers)
        content = BeautifulSoup(resposne.content, 'lxml') # response.text后取得是回复的文本信息，content可以获得其他图片文件等，lxml是使用的解析器
        areas = content.find('ul', {'data-target': "area"}).find_all('a')
        areas.pop(0)  # 删除第一个元素，因为不是有效区域
        for i in areas:
            area = i.get_text()
            link = 'https://xm.lianjia.com' + i.get('href')
            print("开始抓取各页面")
            self.get_pages(area, link)

    # 通过获取某一区域的页数，来拼接某一页的链接
    def get_pages(self, area, area_link):
        resposne = requests.get(area_link, headers=self.headers)
        pages = BeautifulSoup(resposne.content, 'lxml').find('div', {'class':"content__pg"}).get('data-totalpage')
        print(area + "这个区域有" + pages + "页")
        for page in range(1, int(pages)+1):
            url = area_link + 'pg' + str(page)
            print('\r' + "开始抓取第" + str(page) + "页的信息",end='',flush=True)
            self.get_house_info(area, url)

    # 获取某一区域某一页的详细房租信息
    def get_house_info(self, area, url):
        time.sleep(2)
        resposne = requests.get(url, headers = self.headers)
        content = BeautifulSoup(resposne.content, 'lxml')
        lists = content.find('div', {'class': "content__list"}).find_all('div', {'class': "content__list--item"})
        for l in lists:
            title = l.find('a').get('title')
            square = re.findall('(\d*.\d*)㎡', l.find('div').find('p', {'class': "content__list--item--des"}).get_text())[0]
            floor_info = l.find('div').find('p', {'class': "content__list--item--des"}).find('span').get_text()
            total_info = l.find('div').find('p', {'class': "content__list--item--des"}).get_text()
            try:
                floor = re.findall('([\u4E00-\u9FA5]+)', floor_info)[0] # 寻找一切能找到的中文字符
                total_floor = re.findall('(\d+)', floor_info)[0]
            except:
                floor = ''
                total_floor = ''

            price = l.find('div').find('span', {'class': "content__list--item-price"}).find('em').get_text()

            #with open('链家北京租房.txt', 'a', encoding='utf-8') as f:
             #   f.write(
              #      area + ',' + title + ',' + square + ',' + floor + ',' + total_floor + ',' + price + ',' + '\n')
            # 改造一下，直接变成表格数据
            global 区域,标题,面积,楼层,总楼层,价格,小区信息
            区域 = 区域 + [area]
            标题 = 标题 + [title]
            面积 = 面积 + [square]
            楼层 = 楼层 + [floor]
            总楼层 = 总楼层 + [total_floor]
            价格 = 价格 + [price]
            小区信息= 小区信息 + [total_info]
            
            

def main():
    print('start!')
    get = LJ()
    get.get_areas()

if __name__ == '__main__':
    main()
    df = pd.DataFrame()
    df['区域'] = 区域
    df['小区信息'] = 小区信息
    df['标题'] = 标题
    df['面积'] = 面积
    df['楼层'] = 楼层
    df['总楼层'] = 总楼层
    df['价格'] = 价格
df.to_excel('厦门链家租房信息.xlsx',index = None)