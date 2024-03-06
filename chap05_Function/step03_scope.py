'''
scope : 변수의 사용범위 

 - 전역변수 : 전 지역 사용 
 - 지역변수 : 함수 내에서 사용 (함수 호출 종료되면 소멸)
''' 

# 지역변수 : x

def local_func(x) :
    x = 0
    x += 50  
    print('>> local func(x) =', x) 
# 함수 호출 
local_func(x) # 50 

def local_func(x) :
    x += 50  
    print('>> local func(x) =', x) 
# 함수 호출 
local_func(200) # 250 


x = 30 # 전역변수 x 초기화 
# 전역변수 : x
def global_func() :
    global x # 바깥에 있는 변수x를 사용하기 위해 
    # 참고로, 얘는 함수의 인수가 아님..
    x += 50
    print('>> global_func(x) =', x)  

global_func() # 여러번 실행하면 30 + 50 + 50 +...

