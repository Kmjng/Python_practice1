# -*- coding: utf-8 -*-
"""
함수 응용 

1. 텍스트 전처리 함수 정의 
2. 통계 계산 함수 : 표본의 분산/표준편차 
"""

# 1. 특정 패턴을 가진 문자열 추출
def extract_matching_strings(str_list, pattern):
    matching_strings = [st for st in str_list if pattern in st]
    return matching_strings


str_list = ["apple", "banana", "cherry", "kiwi", "lemon"]
pattern = "le"

result = extract_matching_strings(str_list, pattern)
print("매칭된 문자열:", result) # 매칭된 문자열: ['apple', 'lemon']


# 2. 딕셔너리 리스트에서 특정 키의 값 추출
def extract_values_by_key(data_list, key):
    values = [item[key] for item in data_list if key in item]
    return values

data_list = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35}
]
key = "age"

result = extract_values_by_key(data_list, key)
print("추출된 값들:", result) # 추출된 값들: [25, 30, 35]


# 3. 숫자 리스트에서 짝수 필터링
def filter_even_numbers(num_list):
    even_numbers = [x for x in num_list if x % 2 == 0]
    return even_numbers

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(num_list)
print("짝수 리스트:", result) # 짝수 리스트: [2, 4, 6, 8, 10]   


# 4. 통계 처리 함수 : 표본의 분산/표준편차 계산 함수
dataset = [2,4,5,6,1,8]
dataset = [2,4,5,6,1,8]

# 표본 분산과 표준편차 
from statistics import mean, variance, sqrt

# from 모듈 import 함수1, 함수2, 함수3 
# from (1) import (2) -> (1)에서 (2)를 쓰겠다 ~ ★★★

print('표본 분산 =', variance(dataset))
print('표본 표준편차 =', sqrt(variance(dataset)))

'''
표본 분산 = sum((x변량-산술평균)**2) / n-1
표본 표준편차 = sqrt(표본분산)
'''

# 분산과 표준편차 구하는 함수 만들기 ★★★
def var_sd(x): # x는 리스트로 받아야 할 것 
    x_bar = mean(x) # 산술평균 
    j= 0 
    for i in x : 
        # j =sum((i - x_bar)**2) >> 'float' object is not iterable 
        # 그리고 틀렸다. 
        j += (i-x_bar)**2
        var = j /(len(x)-1)
        std = sqrt(var)
    return var, std
var, sd = var_sd(dataset)

print(var, sd)


# 방법 2) 
def var_sd(x): # x는 리스트로 받아야 할 것 
    x_bar = mean(x) # 산술평균 
    diff = [(i-x_bar)**2  for i in x]
    var = sum(diff) /(len(x)-1) # 이거는 되는 이유가, 
    # float로 구성된 list는 iterable하기 때문이다. ★★★
    std = sqrt(var)
    return var, std
var, sd = var_sd(dataset)

print(var, sd)