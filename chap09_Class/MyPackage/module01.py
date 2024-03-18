# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 15:49:05 2024

@author: itwill
"""
def Adder(x,y):
    return x+y
def Sub(x,y):
    return x-y
def Div(x,y):
    return x/y


class Mul:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def multiply(self):
        return self.x * self.y



print(__name__) # 외부에서 호출 시 , 모듈이름이 출력됨. 
