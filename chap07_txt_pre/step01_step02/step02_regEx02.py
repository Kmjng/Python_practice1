# -*- coding: utf-8 -*-


# 정규표현식 관련 모듈 
import re # re.sub(), re.search(), re.compile()


### 3. re.sub(pattern, rep, string) 
# - 문자열(string)에서 패턴과 일치하는 문자를 찾아서 다른 문자 교체(rep) 

st1 = 'test^홍길동 abc 대한*민국 123$tbc 대한*밍국'

text = re.sub('[\^*$]', '', st1)   
# 여기서 ^를 메타문자가 아닌 일반특수문자로 읽기 위해 앞에 역슬래시\ ★★★★
print(text) 
# test홍길동 abc 대한민국 123tbc

# 그럼만약 ???????????
print(re.findall('[대한^민국]+',st1)) # ['^', '대한', '민국', '대한', '국']


### 4. re.search(pattern, string) 
# - 문자열(string)에서 패턴과 일치하는 문자열 검색 - 객체 반환

# 처음부터 일치해야하는 match()와 다르게, 
# 어딘가에 패턴과 일치하는 문자열이 있으면 반환한다.★★★★

# 예) 특정 태그(tag)안에 포함된 문자 반복 여부로 패턴 지정 
tag = "<span> <head>안녕하세요.</head> </span>"
head_tag = re.search("<head>.*</head>", tag) 
head_tag.group() # '<head>안녕하세요.</head>'

head_tag # >> <re.Match object; span=(7, 26), match='<head>안녕하세요.</head>'>

head_tag = re.search("<head>.+</head>", tag)
head_tag.group() # '<head>안녕하세요.</head>'
type(head_tag) # >> re.Match  # Match의 일부분인가보다~
type(head_tag.group()) # >> class 'str'

head_tag = re.search("<head>.?</head>", tag)
head_tag.group() # AttributeError:
    
print(re.findall("<head>.+</head>", tag))  # >> ['<head>안녕하세요.</head>']



### 5. re.compile(pattern) 
# - 패턴을 객체로 생성하고, 정규표현식 메서드로 문자열 처리  



urls = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~']
len(urls) # >> 4

# url 패턴 객체 생성 
url_pat = re.compile('^http://news') # 접두어가 반드시 ^뒤의 문자열들과 같아야한다.
dir(url_pat)
'''
findall() 
match()
search()
sub()
split() 
객체 생성해서 사용 시, 인수하나만 넣으면 됨. 
객체명.메소드(인수)
'''
# 생성한 객체로 여러번 비교 

# url 패턴 반복 사용 

# (1) 
urls_result = []

for url in urls :
    if url_pat.findall(url) : # 패턴객체.메서드(문자열)  
        urls_result.append(url)
        
print(urls_result)    
    


# (1-2)
urls_result = [i for i in urls if url_pat.findall(i)] 
print(urls_result) # >> ['http://news.com/test', 'http://news.com/test2']




# (2) pattern.search(string) 
#  주의 : group()으로 append()하면 패턴과 일치하는 원소만 들어간다 ★★★★
urls2 = ['http://news.com/test', 'new.com','http://news.com/test2', 'http//~', 'sshttp://news.com/test2']
url_pat2 = re.compile('http://news') 
urls_result2 = [i for i in urls2 if url_pat2.search(i)] # i를 append한다.★★★★

# (2-2)
urls_result3 = [i for i in urls2 if re.search('^http://news',i)] 
print(urls_result3) # >> ['http://news.com/test', 'http://news.com/test2', 'sshttp://news.com/test2']



# (2-3)
urls_result4 = [i for i in urls2 if url_pat2.findall(i)] 
print(urls_result4) # >> ['http://news.com/test', 'http://news.com/test2', 'sshttp://news.com/test2']

# (2-4) 틀린 예시 
urls_result5 = []

for i in urls :
    if url_pat.search(i) : # 패턴객체.메서드(문자열)  
        res = url_pat.search(i)    
        urls_result5.append(res.group())
        
print(urls_result5)  # >> ['http://news', 'http://news']


# (3) pattern.split(string) 
string1= '대한민국_end우리나라_end나는'
split_pat = re.compile('_end') 
split_pat.split(string1) # >> ['대한민국', '우리나라', '나는']

# (4) pattern.sub(rep, string)




