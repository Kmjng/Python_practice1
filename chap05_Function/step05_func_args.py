# -*- coding: utf-8 -*-
"""
함수의 가변인수 
 - 한 개 가인수로 여러 개의 실인수를 받는 인수

패킹 (*) : 리스트로 할당함 
근데 함수 파라미터에서 사용할 때에는 * 패킹이 튜플형으로 할당함
리스트로 하고 싶음 ** 로 할당할 것 
"""

# 1. tuple형 가변인수 (매개변수 앞에 * 패킹 표시 ★★)
def func1(name, *names) :
    print(name) 
    print(names) 


# packing ★★
v1 = 10 
lst = [1,2,3,4,5]
v1, *v2 = lst 
print(v1,v2) 
print(type(v2)) # >> class 'list'
# 얘는 *로 패킹했지만, lst가 리스트여서 리스트형이다. 

# 실험 
v1 = 10 
tup = (1,2,3,4,5)
# v1, **v2 = tup >> [오류]
v1, *v3 = tup
print(v1,v3) 
print(type(v3)) # >> class 'list'




# 함수 호출 
func1("홍길동", "이순신", "유관순") # 함수에 인수를 넣었다. 


# 2. dict형 가변인수 
# DB 연동할 때 환경변수 설정을 해주는데 그때 dict형 가변인수를 사용한다고 한다. 

def person(w, h, **other) :
    print('몸무게 :', w)
    print('키 : ', h)
    print('기타 : ', other)     

# 함수 호출
person(65, 175, name='홍길동', addr = '서울시')


# 3. 함수를 인수로 넘기기  
def square(x) : 
    return x**2

def my_func(func, datas) : # (함수이름, 데이터셋)
    calc = []
    for x in datas :  # ★★★★ datas for문 
        calc.append(func(x)) #★★★★ 인수로 들어온 함수 사용 (실질적으로 square())
        # calc.append(square(x)) 이거보다 효율적임
    return calc    

datas = [1,2,3,4,5]
my_func(square, datas) # 외부함수를 실인수로 전달함!!!!!!!!!!wow  



