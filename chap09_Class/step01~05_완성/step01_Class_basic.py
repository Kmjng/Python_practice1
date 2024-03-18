'''
클래스(class)?
 - 여러 개의 함수와 자료를 묶어서 객체(object) 생성 역할
 - 구성요소 : 멤버(변수, 메서드) + 생성자
   -> 멤버변수 : 실세계 상태 
   -> 멤버메서드 :  실세계 동작 
   -> 생성자 : 객체 생성 

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
plus, minus = calc_func(10, 20)
plus() # 30
minus() # -10


# 2. 클래스 : 중첩 함수 -> 클래스 변환 
class Calc_class :
    # 멤버변수=값 : 자료 생성 
    x = None
    y = None 
    
    # 생성자 : 객체 생성 & 멤버변수 초기화 
    def __init__(self, x, y) :
        # 멤버변수 = 매개변수 
        self.x = x 
        self.y = y
    
    # 멤버메서드 : 자료 처리 
    def plus(self):
        p = self.x + self.y
        return p
    
    def minus(self):
        m = self.x - self.y
        return m
    
# 객체 생성 : 생성자 이용 
calc1 = Calc_class(10, 20) # 객체 = 클래스명(실인수) : 생성자 

# 객체 멤버 확인 
dir(calc1)
'''
'minus()', : 메서드(함수)
'plus()',  : 메서드(함수) 
'x', : 필드(자료) 
'y'  : 필드(자료) 
'''

# 객체.멤버(필드+메서드)
calc1.plus() # 30
calc1.minus() # -10
calc1.x # 10
calc1.y # 20

# 필드 값 수정 
calc1.x = 100
calc1.y = 50 

calc1.plus() # 150
calc1.minus() # 50

# 객체 출처 
print(type(calc1)) # <class '__main__.Calc_class'>


# 두번째 객체 
calc2 = Calc_class(100, 200) 

# 객체 멤버 확인 
dir(calc2)
'''
'minus()', : 메서드(함수)
'plus()',  : 메서드(함수) 
'x', : 필드(자료) 
'y'  : 필드(자료) 
'''

# 객체.멤버 
calc2.plus() # 300
calc2.minus() # -100
calc2.x
calc2.y


# 중첩 함수 vs 클래스
'''
공통점 : 자료(data) + 함수(알고리즘) 정의 
중첩함수 : 내부함수 반환 & 호출을 통해서 이용 
클래스 : 객체 반환(자료와 함수 캡슐화) 
'''








      







