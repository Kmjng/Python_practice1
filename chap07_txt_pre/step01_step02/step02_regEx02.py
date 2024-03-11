# -*- coding: utf-8 -*-


# 정규표현식 관련 모듈 
import re # re.sub(), re.search(), re.compile()


### 3. re.sub(pattern, rep, string) 
# - 문자열(string)에서 패턴과 일치하는 문자를 찾아서 다른 문자 교체 

st1 = 'test^홍길동 abc 대한*민국 123$tbc'

text = re.sub('[\^*$]', '', st1)  
print(text) 
# test홍길동 abc 대한민국 123tbc



### 4. re.search(pattern, string)
# - 문자열(string)에서 패턴과 일치하는 문자열 검색  

# 예) 특정 태그(tag)안에 포함된 문자 반복 여부로 패턴 지정 
tag = "<span> <head>안녕하세요.</head> </span>"
head_tag = re.search("<head>.*</head>", tag) 
head_tag.group() # '<head>안녕하세요.</head>'

head_tag = re.search("<head>.+</head>", tag)
head_tag.group() # '<head>안녕하세요.</head>'

head_tag = re.search("<head>.?</head>", tag)
head_tag.group() # AttributeError:




### 5. re.compile(pattern) 
# - 패턴을 객체로 생성하고, 정규표현식 메서드로 문자열 처리  

urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']


# url 패턴 객체 생성 
url_pat = re.compile('^http://news')


# url 패턴 반복 사용 
urls_result = []

for url in urls :
    if url_pat.findall(url) : # 패턴객체.메서드(문자열)  
        urls_result.append(url)
        
        
print(urls_result)        
        
        
        
        
        
        
        
        
        
        










