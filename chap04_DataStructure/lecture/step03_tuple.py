# -*- coding: utf-8 -*-
"""
step03_tuple.py

tuple 특징 
 - 순서 있는 자료구조 
 - 형식) 변수 = (값1, 값2,...)
 - 변경 불가

튜플은 언제 사용하는가? 
요소를 실수로 변경하는 상황을 방지하고자 할 때 사용한다. 

파이썬에만 있는 자료구조
데이터 공간을 미리 할당하는 List(Array)와 다르게 
적고 간단한 데이터를 표현할 때 사용하면 좋다. 
(List(Array)보다 메모리 적게 사용함)
"""

# tuple
tp = (10,) # 원소가 한 개=> 컴마(,)를 사용해야 한다. 
print(tp) # >> (10,)

tp2 = (1,2,3,4,5)
print(tp2)

print(len(tp2), type(tp2)) # 5 <class 'tuple'>

# indexing # 리스트와 동일한 방식
print(tp2[0], tp2[1:4]) # 1 (2, 3, 4)
print(tp2[-1], tp2[-3:]) # 5 (3, 4, 5)


# 객체 제거  
# 수정불가능하기 때문에 아싸리 삭제해준다. 
del tp2
#print(tp2) # name 'tp2' is not defined


# for + tuple
datas = (10, 23.4, 6, 8)

for d in datas :
    print(d*2, end = ' ') # 값만 넘겨서 출력하는 정도로 
    
# 튜플에 있는 원소 리스트에 추가하기     
lst =[]
for i in datas: # 튜플 원소에 대한 for문 
    lst.append(i)

print(lst)


# zip() : tuple 반환 
# 서로 다른 리스트를 1:1로 묶어주는 함수 (튜플로 묶임★) 
names = ['홍길동','이순신','유관순']
dno =[10,20,20]

emp=zip(names, dno) #리스트 길이가 맞아야 함
print(emp)  # >> <zip object at 0x000001DD4C708EC0>

emp2 = list(zip(names, dno))
print(emp2)    

for name, dno in emp :
    print(f'이름: {name}, 부서번호: {dno}')
    
# type은? 
print(type(emp2)) # >> class 'list'이다. 

    




