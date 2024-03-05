# -*- coding: utf-8 -*-
"""
step05_dict.py

dict 특징 
 - 순서 없는 자료구조 (set과의 공통점)
 - key와 value 한쌍 
 형식) {key1:value1, key2:value2, ...}

★★★ 딕셔너리에서는 키(key)가 색인(index) 역할을 한다 ★★

"""

# 1. dict 생성 
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) 
print(len(person), type(person)) # 3 <class 'dict'>


# 2. 수정, 삭제, 추가, 검색 
person['age'] = 45 # 수정 
del person['addr'] # 삭제 
person['pay'] = 350 # 추가 


# 3. for + dict
for key in person.keys() : # key 넘김 
    print(key, end = ' ') # key
    print(person[key]) # value
    
for value in person.values() :  # value 넘김 
    print(value) # value

for item in person.items() : # key+value
    print(item)
    
    
# key 검색 
print('age' in person) # True    


# 4. 단어 빈도수 
charset = ['pay', 'name', 'pay', 'name', 'age']
charset

wc = {} # 빈set 

for ch in charset :
    if ch not in wc : # 사전에 key 유무 
        wc[ch] = 1 # key 없음 
    else :
        wc[ch] += 1 # key 있음 
print(wc) 


# 5. {key : [value1, value2]}
# 예) {'사번' : [급여, 수당]}
emp = {'1001' : [250, 50], '1002' : [200, 40], '1003': [300, 80]}


# key 이용 : 급여 + 보너스 
pay = {'홍길동' : 200, '이순신':250, '유관순' : 200} 
bonus = {'홍길동' : 50, '이순신':80, '유관순' : 30} 





