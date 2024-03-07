# -*- coding: utf-8 -*-
"""
축약함수(Lambda) : 한 줄 함수, 이름없는 함수  
무명함수 
 형식) 변수 = lambda 인수 : 명령문(리턴값) 
명령문 시행 및 반환 (return 이 포함된 기능)
"""

# 1. 일반함수
def Adder(x, y) :
    add = x + y
    return add

Adder(10, 30) # 40
print(type(Adder(10,30)))

# 2. 축약함수(Lambda) class 'function'
Adder2 = lambda x, y : x + y

print(type(Adder2)) # >> class 'function'
print(type(Adder2(10, 30))) # >> class 'int'

print('add =', Adder2(10, 30)) # add = 40


# 함수 정의 & 호출 
(lambda x, y : x + y)(10, 30)


# [실습] x 변량에 제곱 
dataset = [1,2,3,4,5] 

# 일반함수 
def result(data) :
    calc = [x**2 for x in data]
    return calc

print('result :', result(dataset))


# 람다함수
result2 = lambda data : [i**2 for i in data]
# 호출방법 1
result2(dataset) #data 인자에 dataset 인수를 넣는다. ★★★
# 호출방법 2
(lambda data : [i**2 for i in data])(dataset)



'''
python의 한줄 문법 
1. 한 줄 if -> 변수 =  참 if 조건 else 조건 
2. list comprehension -> 변수 = list + for
3. 한 줄 함수 -> 변수 = 람다  또는  (람다)() 
'''

# 중첩 list 내의 원소들 합계(tot) 구하기 
def tot(x) : 
    return sum(x) 

datas = [[1,2,3],[3,4],[1,4]]
len(datas) # >> 3

# list comprehension 
result = [ tot(i) for i in datas ] # 이때 i는 리스트
print(result)

# list comprehension + Lambda function  
result2 = [(lambda i : sum(i))(i) for i in datas]

print(result2)


# 딴짓
a = 511
b = 511 
print(id(a), id(b)) # >> 1842701080368 1842701080016
print(a==b) # >> True ( 값 비교)


