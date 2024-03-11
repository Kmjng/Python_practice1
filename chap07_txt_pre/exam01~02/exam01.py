# -*- coding: utf-8 -*-
"""
문1) 아래 urls 리스트를 대상으로 'http://news'로 시작하는 url만 추출하여 final_urls에 저장하시오. 
     
     힌트) findall()함수와 접두어(^) 이용 
         

   <출력결과> 
 final_urls :  ['http://news.com/test', 'http://news.com/test2']
"""


import re  

urls = ['http://news.com/test','now.co.kr', 'new.com','http://news.com/test2', 'http//~']


final_urls = [] # 옳바른 url 저장 

for i in urls : 
    if re.findall('^http://news', i):
        final_urls.append(i) # urls 이 string 이니까 ★★★★★★★★
print(final_urls)

# 방법2 
final_urls2 = [i for i in urls if re.findall('^http://news',i)]
print(final_urls2)
