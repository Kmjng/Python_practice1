# -*- coding: utf-8 -*-
"""
단어 카운트(word count) 작업절차 
 1. 텍스트 파일 읽기
 2. 텍스트 전처리
 3. 단어 카운트
 4. TopN 단어 선정
"""

import re 

# 텍스트 전처리 함수 정의 
def clean_text(texts) : # list input

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 문장부호 & 특수문자 제거     
    texts_re2 = [re.sub(r'[^\w\d\s]', '', st) for st in texts_re]
    

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [re.sub('[0-9]', '', st) for st in texts_re2]    
   
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [re.sub(r'\s+', ' ', st) for st in texts_re3]

    return texts_re4


# 1. 텍스트 파일 읽기 
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'
file = open(path + '/texts.txt', mode = 'r', encoding='utf-8') 

# with ★★★★ 파일 열고닫고 매번 귀찮으니까 사용
with open(path + '/texts.txt', mode = 'r', encoding='utf-8') as file : 
    texts = file.readlines() # >> file객체를 readlines()하는 객체. class 'list''
    # 블록을 넘어가면 자동으로 닫힘 (객체 소멸)

print(texts)

file.close()

# 2. 텍스트 전처리 
new_texts = clean_text(texts)    
new_texts

# 3 단어 카운트(word count)
words=[]
wc = {} #단어 빈도수
wc2= {}
for i in new_texts:
    for j in i.split():
        words.append(j) 

# 단어 카운트 방법 1
for i in words:
    if i in wc:
        wc[i] += 1
    else : 
        wc[i] =1 
# 단어 카운트 방법 2 
for i in words:
    wc2[i] = wc2.get(i,0) +1  #  get(key, 기본값) 키가 없으면 기본값★★★

print(wc)   
print(wc2)

# 4. TopN 단어 출력  (출현빈도수 top)
# sorted() 주의: sorted(iterable) 리스트도 사용가능 
wc_sorted = sorted(wc,key=wc.get, reverse = True) #wc 딕셔너리에 대해서, key는 wc.get
# key값을 보여준다.
# reverse가 들어오면(True이면) 내림차순 ★★★
print(wc_sorted) 

top5 = wc_sorted[:5]  # 이거 [:5] 뭔뜻이더라 ?????????
top5    # >> ['우리나라', '대한민국', '나는', '만세', '비아그라']

for i in top5: 
    print(i,wc[i], sep='->') # ★★★ print안에서의 구분자
'''
우리나라->2
대한민국->2
나는->2
만세->1
비아그라->1
'''



 