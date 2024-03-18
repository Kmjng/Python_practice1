'''
1. 동적 멤버변수 생성
  - 생성자 또는 메서드에서 동적으로 멤버 변수 생성 
'''

class Car :
    # 멤버변수 정의
    door = 0
    cc = 0
    name = None 
    
    # 생성자 
    def __init__(self, name, door, cc):
        self.name = name
        self.door = door
        self.cc = cc
        
    # 메서드 정의 : 자동차 정보 
    def display(self):             
        print("%s는 %d cc이고, 문짝은 %d개 이다."
              %(self.name, self.cc, self.door))
    

'''
2. 기본 생성자(묵시적 생성자)
  - 생성자를 생략하면 기본 생성자가 만들어진다. 
'''

class default :     
    # 생성자 없음
    
    def data(self, x, y):
        self.x = x
        self.y = y
        
    def mul(self):
        return self.x * self.y
        
        
        
         


