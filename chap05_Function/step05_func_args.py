# -*- coding: utf-8 -*-
"""
함수의 가변인수 
 - 한 개 가인수로 여러 개의 실인수를 받는 인수
"""

# 1. tuple형 가변인수 
def func1(name, *names) :
    print(name) 
    print(names) 

# 함수 호출 
func1("홍길동", "이순신", "유관순")


# 2. dict형 가변인수 
def person(w, h, **other) :
    print('몸무게 :', w)
    print('키 : ', h)
    print('기타 : ', other)     

# 함수 호출
person(65, 175, name='홍길동', addr = '서울시')


# 3. 함수를 인수로 넘기기  
def square(x) : 
    return x**2

def my_func(func, datas) : 
    calc = []
    for x in datas :
        calc.append(func(x))
    return calc    
