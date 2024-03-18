'''
1. 동적 멤버변수 생성
  - 생성자 또는 메서드에서 동적으로 멤버 변수 생성
  
2. self : 자신(현재 클래스)의 멤버(변수, 메서드)를 호출하는 객체   
'''

class Car :    
    # 생성자 : 객체 생성 & 멤버변수 초기화 
    def __init__(self, name, door, cc):
        # 동적 멤버변수 = 매개변수  
        self.name = name
        self.door = door
        self.cc = cc
    
    def kclass(self) :        
        if self.cc >= 3000 :
            self.kind = "대형" # 동적 멤버변수
        else : 
            self.kind = "중소형" # 동적 멤버변수
    
    # 멤버메서드 정의 : 자동차 정보 
    def display(self) :
        self.kclass() # 멤버메서드 호출                     
        print("%s는(%s) %d cc이고, 문짝은 %d개 이다."
              %(self.name, self.kind, self.cc, self.door))
   
# 첫번째 자동차 
car1 = Car('소나타', 4, 2000) # 객체 생성 & 멤버변수 초기화    
dir(car1)

car1.display()
# 소나타는(중소형) 2000 cc이고, 문짝은 4개 이다.

# 두번째 자동차 
car2 = Car('그랜저', 4, 3000)
car2.display()
# 그랜저는(대형) 3000 cc이고, 문짝은 4개 이다.


'''
2. 기본 생성자(묵시적 생성자)
  - 생성자를 생략하면 기본 생성자가 만들어진다. 
'''

class default :     
    # 생성자 없음 : 기본 생성자 제공
    def __init__(self) :
        pass
    
    def data(self, x, y):
        self.x = x
        self.y = y
        
    def mul(self):
        return self.x * self.y
        
 
obj = default() # 기본 생성자 : 클래스명()         

obj.data(10, 20) # 동적멤버변수 생성 
obj.mul() # 곱셈 메서드  

 
    
 
    
 
        

