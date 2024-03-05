# -*- coding: utf-8 -*-
"""
step01_list.py

list 특징 
 - 순서 있는 자료구조
 형식) 변수 = [값1, 값2, ...]
"""

# 1. 단일 list & 색인 
lst = [1,2,3,4,5]
print(lst) # [1, 2, 3, 4, 5]
len(lst) # 5

# 색인(index) : 값의 위치
lst[:] # 전체 원소 
lst[0] # 첫번째 원소 
lst[-1] # 마지막 원소 

# 리스트[start:stop:step]
lst[::2] #[1,3,5]
lst[1::2] #[2,4]
lst[::-1] # 역순 정렬됨


# list + for 이용 
for i in lst : 
    print(i, end = ' ') # 한 줄 중복 출력 


# 2. 중첩 list & 색인 
y = [['a','b','c'], [1,2,3]] 
print(y) 


# 3. list 값 수정(추가, 삽입, 수정, 삭제)
num = ['one', 2, 'three', 4] #여러 타입 / 복합형 자료형 ★
print(num) # ['one', 2, 'three', 4]

# list의 메소드 확인 
dir(num) 
# list객체.메소드() 사용할 수 있다. 


# 1) list 값 추가 #append()메소드
num.append('five') 
print(num) # ['one', 2, 'three', 4, 'five']

# 2) list 값 삭제 
num.remove('three') #remove()메소드
print(num) # ['one', 2, 4, 'five']

# 3) list 값 수정  #색인(index)으로 수정한다. 
num[1] = 'two' 
print(num) # ['one', 'two', 4, 'five']

# 4) list 값 삽입 #insert() 메소드
# 리스트 특정 위치에 삽입하고 싶을 때 ★★★
num.insert(0, 'zero') # ['zero', 'one', 2, 'three', 4]
print(num)

num.insert(-1,'last')  # ['zero', 'one', 2, 'three', 'last', 4]
print(id(num))

# 4. list 연산 
x = [1, 2, 3, 4]
y = [1.5, 2.5]

# 1) list 결합(+) # 원소끼리 더해지는 게 아님
z = x + y 
print(z) # [1, 2, 3, 4, 1.5, 2.5]

# 2) list 확장 
x.extend(y) # 리스트y의 '원소'로 extend 하겠다.
print(x) # [1, 2, 3, 4, 1.5, 2.5]

# 1)은 새로운 객체를 생성하게 되고, 2)는 기존 객체에 추가하는 것

a =[1,2,3]+[1,2,3]
print(a) # [1,2,3,1,2,3]

# 3) list 추가 
# append()에 값이 아닌 리스트객체가 들어가면 리스트 그대로 추가됨
# extend() 처럼 기존 객체에 추가
x.append(y) 
print(x) # [1, 2, 3, 4, 1.5, 2.5, [1.5, 2.5]]

# 4) list 반복(*)
result = y * 2
print(result) # [1.5, 2.5, 1.5, 2.5]
    


# 5. list 정렬 & 색인 반환  

num.reverse() # 배열의 역순정렬(현재 객체 반영) 
 
num = [3,1,5,2]

# 숫자 원소 정렬 
num.sort() #  [1, 2, 3, 5] : 오름차순(현재 객체 반영)
num.sort(reverse=True) # [5, 3, 2, 1] : 내림차순(현재 객체 반영)
print(num)  # [5,3,2,1]

# 민정) 
# sort()메소드는 문자열, 딕셔너리, 셔플에서 사용 불가능하다. 
# sorted()함수를 사용한다. (현재 객체 반영 x)
# 리스트1 = sorted(리스트) # 재선언 형태로 사용


# 값의 색인 반환 
num.index(2) # 2
num.index('2') # ValueError: '2' is not in list

num1 = ['1','2','3']
num1.index('2') # 1

# pop()
num2 = [5,3,2,1]
result = num2.pop(0) #리스트 원소 추출 및 제거 
result # 5
num2 # [3,2,1]

#전체 원소 제거 clear()
num2.clear() 
print(num2) # []



# 6. 빈 list에 값 추가와 원소 찾기 

num = [] # 빈 list : 숫자 저장 

# 임의 숫자 입력 
for i in range(5) : # 0~4
    num.append(int(input())) # 5 개의 숫자 입력 받기 

print(num)

# 숫자 원소 찾기
if int(input()) in num :
    print('숫자 있음')
else :
    print('숫자 없음')


# 7. 복사
# 얕은 복사(주소 복사) vs 깊은 복사(내용만 복사, 다른 주소로 할당됨)
 # 깊은 복사는 import copy 해서 사용함 
 
name = ['홍길동','이순신','강감찬']
print(id(name)) # 2049984645440
name2 = name # 얕은 복사 
print(id(name2)) # 2049984645440
# 주소를 복사했으므로, 가리키는 내용도 같음 
# name2 리스트의 내용 변경 => name1 리스트 내용도 함께 변경됨 ★★★



import copy 
name3 = name2.copy() 
print(name3, id(name3), id(name2)) 
# ['홍길동', '이순신', '강감찬'] 2049984651904 2049984645440




