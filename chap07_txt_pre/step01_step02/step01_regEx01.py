# -*- coding: utf-8 -*-
"""
정규 표현식(Regular Expressions)  
 - 특정한 규칙을 가진 메타문자를 이용하여 패턴을 지정하는 문자열  

[주요 메타문자]
.x : 임의의 한 문자 뒤에 x가 오는 문자열(예 : abc, mbc -> .bc) 
x. : x 다음에 임의의 한 문자가 오는 문자열(예 : t1, t2, ta -> t.) 

^x : x로 시작하는 문자열(접두어 추출) ★★★
x$ : x로 끝나는 문자열(접미어 추출)

x* : x가 0번 이상 반복(없는 경우 포함)
x+ : x가 1회 이상 반복
x? : x가 0 또는 1회 포함 

x{n} : x가 n 연속
x{m, } : x가 m 이상 연속
x{,n} : x가 n 이하 연속
x{m, n} : x가 m~n 사이 연속 

[x] : x문자 한 개 일치  ★★★
[^x] : x문자 제외 ★★★ 주의 
| : or 조건식(예 : [a-z|A-Z]) 
\ : 이스케이프 문자 또는 일반문자를 메타문자로 변환(예: '\d', '\w', '\s')
() : 그룹핑[예 : '([a-z]{3}|\d{3})' ] 
"""

import re # 정규표현식 관련 모듈  

dir(re)
'''
findall() : 패턴과 일치하는 모든 문자열 
match() : 패턴과 문자열 일치 여부 
search() : findall()과 비슷하지만, 부분 문자열을 찾는 기능
split() : 구분자 기준 문자열 분리
sub() : 문자열을 다른 문자열로 교체할 때 
'''




### 1. re.findall(찾고자하는 패턴, 문자열1) 
# - 패턴과 일치하는 모든 문자열1 을 찾아서 list 반환 ★★★★

st1 = '1234 abc홍길동 ABC_555_6 이사도시' 

# 1) 숫자 찾기 : 메타문자([], {}) 이용   
print(re.findall('1234', st1))  # ['1234']
print(re.findall('[0-9]', st1)) # 범위 안에 있는 거 하나하나 list 반환
print(re.findall('[0-9]{3}', st1)) # 범위 내 숫자 3연속을 묶어 list 반환 
print(re.findall('[0-9]{3,}', st1)) #['1234','555']

# 2) 문자열 찾기 : 메타문자(|) 이용 
print(re.findall('[가-힣]{3,}', st1)) # 범위 내 문자 3연속 이상들을 묶어 list 반환 
print(re.findall('[a-z]{3}', st1)) 
print(re.findall('[a-z|A-Z]{3}', st1)) 

tokens = st1.split(sep=' ') #st1 리스트화
tokens

name = [] 
for i in tokens : 
    result = re.findall('[가-힣]{3,}', i)
    print(result)
'''
[]
['홍길동']
[]
['이사도시']
'''
names = [] 
names1= []
for i in tokens : # tokens이 list니까~ extend 해야 중첩리스트가 아닙니다~ ★★★★
    result = re.findall('[가-힣]{3,}', i)
    if result: 
        print(result)
        names.append(result)
        names1.extend(result) 
    else : 
        print('패턴 불일치')

print(names) # >> [['홍길동'], ['이사도시']] append 하면 중첩리스트됨.
print(names1) # >> ['홍길동', '이사도시']
'''
패턴 불일치
['홍길동']
패턴 불일치
['이사도시']
'''

    
# 3) 접두어/접미어, 중간 문자열 찾기 : 메타문자(^, $, .)
st2 = 'test1abcABC 123mbc abbc,ac 45text'  

print(re.findall('^test', st2))  # ['test']
print(re.findall('^text', st2))  # []
print(re.findall('text$', st2))  # ['test']

# 문자열 중간에서 문자 찾기 : 메타문자(.) 
re.findall('.bc', st2) # ['abc', 'mbc', 'bbc']
re.findall('b.', st2) # ['bc', 'bc', 'bb']


# 4) 단어(word) : 메타문자(\w) #  단, 영문, 숫자, 한글 만 해당된다 ★★★★
st3 = 'test^홍길동 abc 대한 민국 123$tbc'

words = re.findall('\w{3,}', st3)
print(words) 


# 5) 문자열 제외 : 메타문자([^제외문자])
print(re.findall('[^t]', st3)) # t를 제외한 나머지 문자 하나씩 반환
'''
['e', 's', '^', '홍', '길', '동', ' ', 'a', 'b', 'c', ' ', '대', '한', 
 ' ', '민', '국', ' ', '1', '2', '3', '$', 'b', 'c']
'''
print(re.findall('[^t]+', st3)) # t제외한 나머지 문자 1개 이상(+) 
# >> ['es', '^홍길동 abc 대한 민국 123$', 'bc']

# 불용어 (특수문자) 제외 
# 불용어 기점으로 끊어낸다. 
re.findall('[^^$]+', st3 ) # 특수문자 ^와 $를 제외하고 반환하겠다. 
# >> ['test', '홍길동 abc 대한 민국 123', 'tbc']
re.findall('[^^%]+', '^asdf fas%    ') # >> ['asdf fas', '    ']
re.findall('[^#%]+', '#asdf fas%    ') # >> ['asdf fas', '    ']


st4 = 'abcABC 123mbc abbc ac 45text'

# 6) 문자 반복 : 메타문자(x*, x+, x?)
# a b * c  = a__c ★★★★★★★
print(re.findall('ab*c', st4)) # ['abc', 'abbc', 'ac']
print(re.findall('abc*','abcABC 123mbc abbc ac 45text')) # ['abc', 'ab']
print(re.findall('*',st4))

print(re.findall('ab+c', st4)) # ['abc', 'abbc'] # abc 찾는 데 가운데 b가 한번 이상 나와야 한다. 

print(re.findall('ab?c', st4)) # ['abc', 'ac'] # abc 찾는 데 가운데 b가 한번 또는 없어야 한다.

tags = "<ul> <li>첫번째목록</li> <li>세번째목록</li> </ul>"

tags = tags.split()
print(tags)

for i in tags: 
    tag = re.findall('<li>.+</li>', i)
    if tag : 
        print(tag)
    else: 
        pass 

re.findall('<li>.+</li>',tags) # . 은 임의의 문자, +는 하나 이상



# 2. re.match(pattern, string) 
# - 패턴과 일치하는 문자열 이면 객체 반환(불일치 NULL 반환) 

jumin = '123456-3234567'

result = re.match('\d{6}-[1-4]\d{6}', jumin) 
# 패터 일치 여부 반환 : 일치 -> object 반환, 불일치 -> NULL 반환 

print(result) # <re.Match object; span=(0, 14), match='123456-3234567'>

# 매칭된 텍스트 반환 
result.group() # '123456-3234567'


if result : # object 반환 : True,  None : False 
    print('주민번호 양식')
else :
    print('잘못된 양식')


