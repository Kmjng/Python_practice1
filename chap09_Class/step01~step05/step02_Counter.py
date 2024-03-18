# -*- coding: utf-8 -*-
"""
계수기(Counter) 클래스 만들기 : ppt.13 참고 
  구성요소 : 멤버변수 1개, 멤버메서드 3개   
"""

class Counter:
    count = None # 멤버변수
    
    def __init__(self) :
        self.count = 0 # 멤버변수 초기화
        
    def reset(self) :
        self.count = 0
        
    def increment(self):
        self.count += 1
        
    def get(self):
        return self.count