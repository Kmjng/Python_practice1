# -*- coding: utf-8 -*-
"""
step02_list_for.py

리스트 내포(comprehension) 
 - list안에서 for와 if문을 한 줄로 표현한 문법

 형식1) 변수 = [실행문  for 변수 in 열거형객체]       
 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]   
 형식2-2) 변수 = [실행문 if 조건식1 else 실행문2 for문]
# if 조건식에 만족하면 실행문, False면 for문으로 돌아간다. 
# ★★★ Algorithm : 1. for문 >> 2. if문 >> 3. expression ★★★




"""

nums = list(range(1,11))
print(nums)
result =[]
for n in nums : 
    result.append(n**2) 
print(result)

# 위의 표현식을 리스트 컴프리핸션으로 써보면 다음과 같다. 
result= [n**2 for n in nums] # n**2 실행 및 저장 


# 형식1) 변수 = [실행문  for 변수 in 열거형객체] 
# 입력 데이터와 출력 데이터 길이가 같은 경우 
# x변량에 제곱(**) 계산 예
x = [2, 4, 1, 5, 8]

print(x ** 2) # TypeError: 리스트에 산술연산은 각각의 요소에 수행해줘야 한다.

# list + for 예   
lst = [] # 계산결과 저장 
for i in x : # 주의: i는 리스트 x의 원소임(인덱스 아님~)
    lst.append(i**2)
    print(i)

lst # [4, 16, 1, 25, 64]

# x의 각 변량에 홀짝 판별하기
# 형식2-2)  
lst2 = ['짝수'  if n%2 ==0 else '홀수' for i in x]
# 여기서 if문이 실행문임 

# list 내포 
lst = [i ** 2 for i in x]
print(lst)



# 형식2) 변수 = [실행문  for 변수 in 열거형객체 if 조건식]
# 입력과 출력의 길이가 서로 다른 경우
dataset = list(range(1, 101)) # 100개의 원소 

#  list+for : 10배수 값만 저장  
result = []

for data in dataset :
    if data % 10 == 0 :
        result.append(data)
        
print(result) # 10개의 원소 

result2 = [i for i in dataset if i%10 == 0]

print(result2)

# 형식3) 변수 = [실행문 for문1 for문2 ] #이중 for문
# Algorithm : 1.for문1 > 2.for문2 > 3.실행문 

texts = '''우리나라 대한민국
나는 홍길동 입니다.'''

words = [j for i in texts.split(sep='\n') for j in i.split(sep=' ')]
print(words)





    