# -*- coding: utf-8 -*-
"""
step04_set.py

set 특징 
 - 순서 없는 자료구조
 - 중복은 걸러서 저장된다.  
  형식) 변수 = {값1, 값2,...} #들어가는 순서이지 순서에 의미가 없음

"""

# 1. set 생성 
st = {1, 3, 5, 1, 5} # 중복은 거른다.
print(st, len(st)) # {1, 3, 5} 3 #무작위 순서로 추출

# for + set
for s in st :
    print(s, end = ' ') # 1 3 5
    
    
# 2. 중복 불가 
gender = ['남','여','남','여'] # list
gender

# list -> set
# ★★★ 중복데이터를 제거하는 기능을 한다. ★★★
sgender = set(gender)
print(sgender, type(sgender)) # {'남', '여'} , class 'set'

sgender2 = list(sgender) # 다시 리스트화 
print(sgender2, type(sgender2)) # ['남', '여'] , class 'list'

# 집합관련 
set1 = {1, 3, 4, 5, 7}
set2 = {3, 5}

set1.union(set2) #  합집합 (|): {1, 3, 4, 5, 7}
set1.difference(set2) # 차집합 (-): {1, 4, 7}
set1.intersection(set2) # 교집합 (&): {3, 5}

lst = list(range(100))
spop = set(lst) # 모집단을 set로 

diff = set([3,7,9]) # 또는 diff = {3,7,9}

result = spop.difference(diff) # 0~99 에서 3,7,9 원소가 빠짐 
print(result) 

# 원소 추가 
set2.add(7)
print(set2) # {1, 3, 5, 7}

# 원소 삭제 
set2.discard(7) 
print(set2) # {1, 3, 5}






