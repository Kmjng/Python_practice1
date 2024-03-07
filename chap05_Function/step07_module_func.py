# -*- coding: utf-8 -*-
"""
함수 유형 : 사용자정의함수, 모듈 함수(lib)
모듈(module) 
  - 파이썬에서 제공되는 파일(*.py) 
  - 함수와 클래스 제공 

모듈 함수  
 - 파이썬 제공 함수 
 1. 내장함수: import 없이 바로 사용가능한 함수 
 2. 외장함수: 
"""

# 1. built-in 모듈 (내장함수의 모듈이름이 builtins 임)
dataset = list(range(1,6))
print(dataset) 

# built-in 모듈 제공 내장함수  
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))
print('len=', len(dataset))



# 2. import 모듈 
import statistics # 수학/통계 함수 사용(statistics.py) - 방법1)
print('방법1-평균 : ', statistics.mean(dataset))
print('방법2-평균 :', mean(dataset)) # 안될것이다.




from statistics import mean, median, stdev # - 방법2)  

print('방법1-평균 : ', statistics.mean(dataset))
print('방법2-평균 :', mean(dataset))

print('중위수 : ', median(dataset))
print('표준편차 :', stdev(dataset))

from statistics import * # 비효율적인 방법 #전부 다 메모리로 올라감 



