'''
클래스(class)?
 - 여러 개의 함수와 자료를 묶어서 객체 생성 역할

 형식)
class 클래스 :
     멤버변수=값
     def 생성자(self) :
          멤버변수 초기화  
     def 멤버메서드(self) :
          명령문       
'''

# 1. 중첩 함수
def calc_func(a, b): # outer 함수 : 자료 생성 
    x = a # 10
    y = b # 20
    
    # inner 함수 : 자료 처리 
    def plus():
        p = x + y
        return p
    
    def minus():
        m = x - y
        return m
    return plus, minus # inner 함수 반환
    
# outer 함수 호출 
calc_func(10, 20)


# 2. 클래스 : 중첩 함수 -> 클래스 변환 

      
