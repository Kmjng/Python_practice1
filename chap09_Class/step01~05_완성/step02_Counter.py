# -*- coding: utf-8 -*-
"""
계수기(Counter) 클래스 만들기 : ppt.13 참고 
  구성요소 : 멤버변수 1개, 멤버메서드 3개   
"""

# 1. 계수기 설계도 
class Counter:
    count = None # 멤버변수 : 계수값 
    
    # 생성자 : 객체 생성 & 멤버변수 초기화
    def __init__(self) : 
        self.count = 0 # 멤버변수 초기화
        
    # 멤버메서드 
    def reset(self) : # 초기화 기능 
        self.count = 0
        
    def increment(self): # 시작 기능 
        self.count += 1
        
    def get(self):
        return self.count # 보이는 기능 
    
# 2. 계수기 생성(객체 생성)
counter1 = Counter() # 생성자  

dir(counter1)
'''
 'count', : 멤버변수 -> 필드(자료)  
 'get',   : 멤버메서드 -> 메서드(기능)
 'increment', : 멤버메서드 -> 메서드(기능)
 'reset' : 멤버메서드 -> 메서드(기능)
 '''

counter1.get() # 0

for i in range(10) : 
    counter1.increment() # 계수값 증가 

counter1.get() # 10

counter1.reset() # 초기화 

counter1.get() # 계수값 확인 









    
    
    
    
    
    
    
    