'''
문6) 다음과 같은 조건으로 모듈을 추가하고, 결과를 확인하시오.
   모듈 위치 : myPackage 패키지 
   모듈명 : module02.py
   함수 정의 : 사칙연산 수행 함수 (Add, Sub, Mul, Div)   
   사칙연산 함수 호출하여 결과 확인
  
    <<출력 결과 예>>
  x = 10; y = 5 일 때
  Add= 15
  Sub= 5
  Mul= 50
  Div= 2.0
'''
import os

os.chdir(r'C:/ITWILL/2_Python/workspace/Python_practice1/chap09_Class')
from MyPackage.module01 import Adder, Mul, Sub, Div


x , y = 10, 5
mul = Mul(x,y)
print('Add ={0}\nSub ={1}\nMul ={2}\nDiv ={3}'.format(Adder(x,y), Sub(x,y),mul.multiply(),Div(x,y)))

print(__name__)
