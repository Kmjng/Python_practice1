'''
클래스멤버★와 인스턴스멤버★ 
 1. 클래스(class) 멤버 : 클래스로 호출할 수 있는 클래스변수와 클래스메서드를 의미
    형식) 클래스명.변수 or 클래스명.클래스메서드() 

 2. 인스턴스(instance) 멤버 : 객체로 호출할 수 있는 속성(필드)와 메서드를 의미
    형식) 객체.필드 or 객체.메서드()

함수 장식자 붙어있는 곳에 클래스 매서드 

'''

class MathClass :
    # 클래스 선언부 : 클래스 변수  
    x_class = 100
    y_class = 50
    
    def __init__(self, x, y) :
       # 동적멤버변수 : 인스턴스 변수  
       self.x_ins = x
       self.y_ins = y

    #★★ @classmethod는 파이썬의 내장 함수 장식자(decorator) 중 하나 
    # 클래스 메소드 만들어줄 때 함수 장식자를 활용한다. 
    #  클래스 메서드는 클래스 자체에 영향을 주는 동작을 정의하는데 사용됩니다.
    @classmethod 
    def add(cls) :  # 클래스 메소드
        return cls.x_class + cls.y_class

    @classmethod
    def subtract(cls) :  # 클래스 메소드
        return cls.x_class - cls.y_class

    def multiply(self) :   # 인스턴스 메소드
        return self.x_ins * self.y_ins

    def divide(self) :     # 인스턴스 메소드
        return self.x_ins / self.y_ins
    

# 1. 클래스 맴버 : 클래스명.맴버 
dir(MathClass)
'''
 'add',  # 클래스 매서드
 'divide',
 'multiply',
 'subtract',
 'x_class',   # 클래스 변수
 'y_class']
'''

MathClass.add() # 150
MathClass.x_class # 100

MathClass.divide() # TypeError

# 2. 인스턴스 맴버 : 객체명.맴버  # 클래스 멤버도 호출 가능함
math1 = MathClass(120,11) # 객체 생성해줘야 함
dir(math1) 
'''
 'add',    # 클래스 맴버
 'divide',   # 인스턴스 맴버
 'multiply',  # 인스턴스 맴버
 'subtract',  #클래스 맴버
 'x_class',   #클래스 맴버
 'x_ins',     #인스턴스 맴버
 'y_class',   #클래스 맴버
 'y_ins']     #인스턴스 맴버
'''
math1.divide() # 120/11 >> 10.9090...
math1.add() # 100+50 >> 150 >> 클래스맴버변수로 실행함~~


