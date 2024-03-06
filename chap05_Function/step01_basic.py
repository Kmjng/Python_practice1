# -*- coding: utf-8 -*-
"""
1. 함수(function) : 어떤 기능을 정의해 놓은 것 


2. 사용자정의함수  
 형식)
 def 함수명(인수) :
     실행문
     실행문
     return 값
"""

# 1. 인수가 없는 함수 
def userFunc1() :
    print('userFunc1')
    print('인수가 없는 함수')

# 함수 호출하기 
userFunc1()

# 2. 인수가 있는 함수 
def userFunc2(x, y) :
    z = x + y # 함수 내에서 선언된 변수는 지역변수이다. 
    print('z=', z)

# 함수 호출하기 
userFunc2(10,30)

print(id(userFunc2(10,30))) # >>140728855456496
print(id(userFunc2(656,40))) # >>140728855456496 
# return이 따로 없어서 주소 하나로 쓰는 듯?
print(type(userFunc2(10,30))) # class 'NoneType 
# return 이 따로 없어서 그런가 

# 3. return 있는 함수 
def userFunc3(x, y) :
    add = x + y
    sub = x - y     
    mul = x * y
    div = x / y
    return add, sub, mul, div # 여러개 값 반환 

print(type(userFunc3(10,20))) # class 'tuple'

print(userFunc3(10,20)) # (30, -10, 200, 0.5)

print(id(userFunc3(10,20))) # >>2300905019232
print(userFunc3(10,30)) # (40, -20, 300, 0.3333333333333333)
print(id(userFunc3(10,30)))  #2300902112560

# return 있는 함수 2 
def userFunc4(x, y) :
    z = x + y
    return z  # int형 반환

print(userFunc4(10,20))
print(type(userFunc4(10,20))) # >> class 'int'
print(id(userFunc4(10,20))) #140728856843976
print(id(userFunc4(532,20))) # 2300904186288 


# return이 필요한 경우 예 
def tot_x(x) : 
    tot = sum(x) #이렇게 되면 x는 iterable이어야 겠다. 
    return tot 

def avg_x(x): 
    tot = tot_x(x)  # tot_x() 함수의 리턴값을 가져와서 사용
    avg = tot / len(x) 
    print('avg = ',avg)
    
x = range(1,101)



# 1, 2차 방정식
def fx(x): 
    y1 = 2*x +3 # 1차방정식 (직선)
    y2 = 2*x**2 + 2*x +3 #2차방정식 (곡선) 
    return y1, y2 

# 함수 fx 호출 
fx(1) 
fx(2)


# 
x = list(range(1,11))
y = [fx(i) for i in x ]
print(y)

print(type(y)) # >> class 'list'
y #(5, 7),(... (1차방정식, 2차방정식)

y1 = [i[0] for i in y ]
y2 = [i[1] for i in y ]

import matplotlib.pyplot as plt 
# 그래프를 그리는 데 사용되는 pyplot 모듈
# matplotlib 라이브러리에는 pyplot 외에 
# 색상 맵(color map), 그림 설정(configuration) 및 다른 유용한 도구도 포함
help(plt.pyplot)

help(plt.plot) # plot() 메소드
'''
Help on function plot in module matplotlib.pyplot:

plot(*args, scalex=True, scaley=True, data=None, **kwargs)
    Plot y versus x as lines and/or markers.
'''


plt.plot(x, y1) # matplotlib 라이브러리의 ㅡpyplot의 plot 
plt.title('line')
plt.show() 

plt.plot(x, y2) 
plt.title('curve')
plt.show() 



