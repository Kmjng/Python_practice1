# -*- coding: utf-8 -*-
"""
중첩함수(nested function)

형식)
def outer(인수) :
    명령문
    def inner(인수) :  # 밖에서는 안쪽에서 생성된 함수 호출 불가능
        명령문
    return inner

"""

# 1. 중첩함수 예
def a() : # outer
    print('a 함수')
    
    def b() : # inner 
        print('b 함수')
        
    return b # 내부함수 b를 리턴한다. 
        # '클로저'라고 한다. 

# 외부함수 호출 
a() # 안의 명령문들이 실행되고, 클로저 반환
b=a()  # >> a 함수 
c = b() # >> b 함수 

# 2. 중첩함수 응용 
'''
 - outer 함수 역할 : dataset 생성, inner 함수 포함 
 - inner 함수 역할 : dataset 조작
ex) ATM : 잔액(data), 잔액 조작 함수(확인, 입금, 출금) 
'''
# 함수1, 함수2에 대해 같은 데이터를 사용하고 싶을 때 중첩 함수 사용하는 듯 

def outer_func(data) : # outer 함수 
    dataset = data # dataset 생성 
    #★★ 공용 사용 데이터를 바깥 함수에 정의 ★★★
    
    # inner 함수 
    def tot() : # 합계
        tot_val = sum(dataset)
        return tot_val

    def avg(tot_val) : # 평균 
        avg_val = tot_val / len(dataset)
        return avg_val        
    
    return tot, avg # inner 함수 반환 

data = [1,2,3,4,5]

# (1) 외부함수 호출 
# ★★★ 리턴값이 두개이니까 두 변수(함수)에 선언
a, b = outer_func(data) # 저장하고, 클로저(tot, avg) 반환됨 (단, 그 내부함수를 정의하기만 함)

# (2) 합계를 구하는 내부함수 호출하기 
a()  # >> 15 
print(a())

# (3) 평균을 구하는 내부함수 호출하기 
b() # >> outer_func.<locals>.avg() missing 1 required positional argument: 'tot_val'
b(a()) # >> 3.0 

# 3. nonlocal 명령어 
'''
nonlocal : 내부함수에서 외부함수의 자료를 변경하려고 할 때 해당변수 앞에 붙여준다. 

'''

def main_func(num) : # outer
    num_val = num # data 생성 
    
    # inner 
    def get_func() : # 값 획득 : 획득자 
        return num_val  
    
    def set_func(value) : # 값 지정 : 지정자 
        nonlocal num_val # 지역변수가 아닌 바깥함수의 변수라는 것을 표현 ★
        num_val = value  
        
    return get_func, set_func

# (1) 외부함수 호출 
a, b = main_func(100) # 100이 들어가고, 두개의 내부함수 정의하고 클로저 리턴

a()  # 100  #내부함수1 (획득자; getter)
b(a())  # 내부함수2 (지정자; setter)
a() #100
b(200) # 리턴값은 없지만 다음 내부함수 실행하면 b(200) 실행값(value에 200)이 들어감
a() # 200 

'''
ATM : 잔액(data), 잔액 조작 함수(확인, 입금, 출금)
'''
def ATM(bal): 
    balance = bal # 잔액 data 
    
    # inner ft 
    def get_bal(): # 확인 # 획득자 getter #nonlocal 안해줘도 됨
        return balance 
    def deposit(price): # 입금 # 지정자 setter 
        nonlocal balance
        balance += price
        return balance
    def withdraw(price): # 출금 # 지정자 setter 
        nonlocal balance
        balance -= price
        return balance
    return get_bal, deposit, withdraw

ATM(10000) # 만원 
get_bal, deposit, withdraw = ATM(10000)
print( get_bal) # <function ATM.<locals>.get_bal at 0x000001AD098C32E0>
 #  함수를 디버깅하거나 추적할 때 쓰임.
print(get_bal()) # 10000

deposit(50000)

