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


import re 
# 1.파일 읽기 : obama.txt
path = r'C:\ITWILL\2_Python\workspace\Python_practice1\chap06_File\data'

with open(path+'\obama.txt', mode = 'r') as rfile :
    lines = rfile.readlines()


# 2. 줄단위 전체 읽기 
print(lines)

# 3.줄 단위 텍스트 전처리         
def text_pre(texts): 
    texts= [i.strip() for i in texts] 
    texts1 = [i.lower() for i in texts]
    texts2 = [re.sub(r'[^\w\d\s]','',i) for i in texts1] #  앞에 r붙는 것은 이스케이프 문자가 아니라 메타문자라는 것을 명시하기 위해  
    # texts2 = [re.sub('\n','',i) for i in texts1] 왜 대체안되는지 아직 모르겠지만, 일단 먼저 줄바꿈 자체를 제거해줘야함..
    
    return texts2

result_line = text_pre(lines)
print(result_line)
# >> ['', ' obama hello skybrook', '', 'applause', '', 'its good to be home', '', 'applause', '', 'thank you everybody',....]

# 4. 단어 카운트 : 전체 단어수 & 최고 단어 
words = {} 
for i in result_line:
    for j in i.split():
        words[j] = words.get(j, 0) +1  #나는 한번에 해서 중복단어가 빠짐!!!!
print(words)

words_sorted = sorted(words,key = words.get, reverse = True)   # value로 정렬할거임
print(words_sorted)

words_max = max(words, key = words.get) # 이때 key반환됨
print('전체단어수:',len(words),'\n최빈단어:', words_max) # 중복단어가 빠져서 전체단어수 1430 개, 최빈단어: the

# 최빈단어의 수는 max()해서 value값 가져와야함. 
words_max2 = max(words.items(), key = lambda x : x[1]) # x[1] value기준, x[0] key 기준
print(words_max2) # >> ('the', 206)   type tuple 

# 5. Top10 단어 & 단어 빈도수 
top_10  = words_sorted[:9]
print(top_10) # >> ['the', 'and', 'of', 'to', 'our', 'that', 'you', 'a', 'we']

for i in top_10 : 
    print(f"{i}: {words[i]}") # key가 i랑 일치하는 ~
'''
the: 206
and: 195
of: 152
to: 140
our: 109
that: 91
you: 83
a: 83
we: 81

'''


# test....

st1 = r'asdf\n'
print(st1) # >> asdf\n
print(re.sub(r'\\n','',st1)) # >> asdf

st2 = 'asdf\nqwer' # 이스케이프문자
print(st2) # >> asdf    qwer
print(re.sub(r'\n','',st2)) # >> asdfqwer
print(re.sub(r'\n','',st2)) # >> asdfqwer

# test2 
st3 = '라가나다'
print(re.findall('[나가]',st3)) # >> ['가', '나'] 
print(re.findall('가나',st3)) # >> ['가나']
# test3 





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

'''
lambda 함수 활용 딕셔너리 정렬 
'''
test1 = {'1':'b', '2':'z', '3':'x','5':'t','9':'a','7':'a'}



t = sorted(test1, key = lambda x : x[0], reverse = False) 
print(t) # >> ['1', '2', '3', '5', '7', '9']

t1 = sorted(test1, key =test1.get, reverse = False) # value 정렬 - .get 메소드로 value 가져옴
print(t1) # >> ['9', '7', '1', '5', '3', '2']

t2 = sorted(test1.items(), key = lambda x : x[1], reverse = False) # value 정렬 - items()로 value 가져옴
print(t2) # >> [('9', 'a'), ('7', 'a'), ('1', 'b'), ('5', 't'), ('3', 'x'), ('2', 'z')]
    
t3 = sorted(test1.items(), key = lambda x : (x[1],x[0]) , reverse = False) # value, key 정렬 - items()로 value 가져옴
print(t3) # >> [('7', 'a'), ('9', 'a'), ('1', 'b'), ('5', 't'), ('3', 'x'), ('2', 'z')]
    # lambda 안에 괄호는 매개변수 감싸는 용도임
    
