# -*- coding: utf-8 -*-
"""
문4) json 형식을 갖는 labels.json 파일을 읽어와서 다음과 같이 처리하시오.
    단계1> 전체 행을 대상으로 url 자료를 추출하여 list에 저장  
          -> 'url'키를 이용하여 url자료 추출한다.(url'키가 없는 경우를 대비하여 예외처리)  
    단계2> list에 저장된 url 자료를 배열(Array) 형식으로 json 파일(urls_data.json)에 저장      
"""

import json

path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'


# [단계1] json file 읽기 (보니까, 대괄호(배열)로 되어 있음★★)
file = open(path + "/labels.json", mode='r', encoding='utf-8') 
lst1= json.load(file) # json파일 디코딩하기
print(lst1, len(lst1), type(lst1)) # .... 30 class 'list'

file.close()
# [단계2] url 자료 추출 
urls = [] # url 저장 
type(lst1[0]) # >> class 'dict'

for i in lst1: # i는 dict 
    try:     
        urls.append(i['url'])  # 주의 ★★★★
    except : 
        pass 
print(urls, type(urls), len(urls)) # .... <class 'list'> 30

# [단계3] json file 쓰기(저장)  - 배열 형태로 인코딩하기★★

file2 = open(path+'/urls_data2.json', mode = 'w') #urls_data.json 파일 생성 
json.dump(urls, file2)

file2.close() 


