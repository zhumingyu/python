#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : douban_250.py
# Date              : 16.11.2018
# Last Modified Date: 16.11.2018
#  https://blog.csdn.net/m0_37788308/article/details/80378042
"""爬取豆瓣movies top250"""
from lxml import etree
import requests
for a in range(10):
    url = 'https://movie.douban.com/top250?start={}'.format(a*25)
    data = requests.get(url).text
    s = etree.HTML(data)
    #  title = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    #  score = s.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
    file = s.xpath('//*[@id="content"]/div/div[1]/ol/li')
    for div in file:
        #  电影名称
        movies_name = div.xpath('./div/div[2]/div[1]/a/span[1]/text()')[0]
        #  评分
        movies_score = div.xpath('./div/div[2]/div[2]/div/span[2]/text()')[0]
        #  URL链接
        movies_href = div.xpath('./div/div[2]/div[1]/a/@href')[0]
        #  评论数
        movies_number = div.xpath('./div/div[2]/div[2]/div/span[4]/text()')[0]
        #  描述
        movies_scrible = div.xpath('./div/div[2]/div[2]/p[2]/span/text()')
        #  print(len(movies_scrible))
        #  print(movies_scrible)
    #  for i in range(25):
        #  print("{} {}".format(title[i], score[i]))
       #  [TODO]出现不匹配问题待处理
    if len(movies_scrible) > 0:
        print("{} {} {} {} {}".format(movies_name, movies_href, movies_score, movies_number, movies_scrible))
    else:
        print("{} {} {} {}".format(movies_name, movies_href, movies_score, movies_number))
