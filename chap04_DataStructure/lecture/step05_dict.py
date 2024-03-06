# -*- coding: utf-8 -*-
"""
step05_dict.py

dict 특징 
 - 순서 없는 자료구조 (set과의 공통점)
 - key와 value 한쌍 
 형식) {key1:value1, key2:value2, ...}

★★★ 딕셔너리에서는 키(key)가 색인(index) 역할을 한다 ★★

    - key는 중복 불가능이다. 
"""

# 1. dict 생성 
person = {'name':'홍길동', 'age':35, 'addr':'서울시'}
print(person) 
print(len(person), type(person)) # 3 <class 'dict'>
# 딕셔너리 자료의 길이는 key1:value1 의 갯수 

# 2. 수정, 삭제, 추가, 검색 
'''
색인 연산자 : []
list[정수색인]vs dict['key']

'''
person['age'] = 45 # 수정 
del person['addr'] # 삭제  (튜플은 한번에 del하고, 딕트는 선택적del 가능)
person['pay'] = 350 # 추가 # 딕트명[키]=값

if 'pay' in person : # [default] person.keys()
    print('pay라는 키가 있습니다.')
else: 
    print('키 없습니다.')


# 3. for + dict
# ★★ key 또는 value를 호출/연산 등에 사용하려면, 
# person.keys(), person.values() 처럼 내용을 넘겨줘야 함
# 생략하면 디폴트 person.keys() 로 설정되어 있음

for key in person.keys() : # key 넘김 
    print(key, end = ' ') # key
    print(person[key]) # value
    
for value in person.values() :  # value 넘김 
    print(value) # value

for item in person.items() : # key+value
    print(item)
    
    
# key 검색 
print('age' in person) # True    


# 4. 단어 빈도수 (word counter 만들기)
charset = ['pay', 'name', 'pay', 'name', 'age']
charset
print('pay' in charset) # True 

wc = {} # 빈set 
# 뭘 추가하느냐에 따라 set인지, dict인지 결정됨


# 방법 1) key 검색 이용
for ch in charset :
    if ch not in wc : # 사전에 key 유무 
        wc[ch] = 1 # key 없음 
    else :
        wc[ch] += 1 # key 있음 
print(wc) 

# 방법 2) get(key, 기본값) 메소드 이용 
help(wc.get)
'''
Return the value for key 
if key is in the dictionary, else default.
'''
wc ={}
for i in charset :
    wc[i] = wc.get(i, 0) +1  




# 딕셔너리는 키(key)는 중복이 안됨 ★★
# 그리고 같은 키를 갖는 values들에 대해서는 
# 나중에 들어온 값이 덮어쓰게 된다. 

# 5. {key : [value1, value2]}
# 예) {'사번' : [급여, 수당]}
emp = {'1001' : [250, 50], '1002' : [200, 40], '1003': [300, 80]}

print(len(emp))

for eno, price in emp.items(): #for 첫번째 인자가 key, 두번째가 value
    print(eno, price)

# 급여(value의 0번째 값)이 250 이상인 사원번호(key) 반환하기 
for eno, price in emp.items():
    if price[0] >= 250 : 
        print(eno)


# key 이용 : 급여 + 보너스 
pay = {'홍길동' : 200, '이순신':250, '유관순' : 200}
bonus = {'홍길동' : 50, '이순신':80, '유관순' : 30}

tot_price=[]
for ename in pay.keys():
    tot = pay[ename]+bonus[ename]
    # 주의: bonus 딕트는 pay와 같은 key 이름들을 공유하고 있어서 가능
    tot_price.append(tot)
print(tot_price)


# 6. 가변수(dummy) 와 인코딩 with Dictionary 

# 1) 혈액형 가변수 만들기 
blood_map = {'AB':1, 'A':0, 'B':0, 'O':0}

datas =['A','B','AB','O','A'] #이와 같은 데이터셋이 들어오면? 

# 리스트 컴프리핸션 
blood_dummy = [blood_map[i] for i in datas]
# 리스트안의 요소들을 key로 해서 value 반환 
print(blood_dummy)
# [0, 0, 1, 0, 0] # 인코딩

# 2) label 인코딩 : 출력 자료 
# 인코딩을 벡터로 이진수 표현하면 원핫인코딩(one-hot encoding)
# 임베딩: 토크나이즈된 토큰들을 벡터화 - 차이점은? 
'''
원핫 인코딩은 카테고리형 데이터를 다룰 때 사용되며, 
orthogonal하게 저장되기 때문에 나중에 유사도거리 구할 때 어려움이 있음.
그리고 범주의 개수 만큼의 차원을 가짐 

임베딩은 Dense한 벡터로 표현해서 모델의 일부로서 학습됨
'''

# 원핫인코딩 실습
label_map = {'thin':[1,0,0], 'normal':[0,1,0], 'fat':[0,0,1]  }

# 우리의 데이터와 다음과 같다고 하자 .
datas = ['normal','fat','normal','thin','fat']

label_encoding = [label_map[i] for i in datas] # list comprehension 

print(label_encoding)



