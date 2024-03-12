# -*- coding: utf-8 -*-
"""
문6) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.
  
  <출력 예시>  
전체 단어수 = 4,907개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 205
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""

from re import sub

# 텍스트 전처리 함수
def clean_text(texts) : # list input
    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 특정 문자나 기호들을 제거     
    texts_re2 = [sub(r'[^\w\d\s]', '', st) for st in texts_re]
    

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [sub('[0-9]', '', st) for st in texts_re2]    
   
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [sub(r'\s+', ' ', st) for st in texts_re3]

    return texts_re4



# 1.파일 읽기 : obama.txt
path = r'C:\ITWILL\2_Python\workspace\chap06_try_FileIO\data'
rfile = open(path + '/obama.txt', mode = 'r') 


# 2. 줄단위 전체 읽기 

# 3.줄 단위 텍스트 전처리         

# 4. 단어 카운트 : 전체 단어수 & 최고 단어 
    
# 5. Top10 단어 & 단어 빈도수 
 




# 실습 obama.txt 
# 민정 - 전처리 함수를 안만들고 했음..
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'

with open(path+'/obama.txt',mode = 'r', encoding='utf-8') as file2:
    lines = file2.readlines()

print(lines)

words_list = []
words_cnt = {}
for i in lines: # 리스트에 대한 string들 하나씩 보겠다. 
    i = re.sub(r'[^\w\d\s]','',i) # 불용어 제거
    if re.search(r'[^\n]',i):
        words_list.append(i.split())
    else : 
        pass 
print(words_list)

print(words_list[0])

for i in words_list:
    for j in i :
        words_cnt[j] = words_cnt.get(j,0) + 1


print(words_cnt)
print(len(words_cnt)) # >>> 1496 

del words_cnt['APPLAUSE']

words_cnt_sorted = sorted(words_cnt, key=words_cnt.get, reverse = True)

print(words_cnt_sorted)

top_10 = words_cnt_sorted[:10]
print(top_10)

print("최고단어: ", max(words_cnt, key=words_cnt.get))
for i in top_10 : 
    print(i, words_cnt[i], sep='->')


