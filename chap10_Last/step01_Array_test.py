# -*- coding: utf-8 -*-
"""
주요 코딩 테스트 영역 
1. 배열 자료 처리 : 리스트와 같은 배열의 자료를 주어진 조건으로 처리
2. 수치 연산 : 피보나치 수열, 팩토리얼 계산  
3. 자료구조 : 자료정렬 및 검색 
4. 문자열 처리 : 불용어 및 중복문자 제거, 중복문자 카운트   
"""


### 1. 배열 자료 처리 : 최댓값/최솟값, 두 수 합, 중복제거, 빈도수 찾기, 회전 

# [1] 주어진 정수 배열에서 가장 큰 두 수의 합을 찾는 함수
def find_largest_sum(nums) :
    
    max_val1 = max_val2 = 0
    
    for num in nums :
        if max_val1 < num :
            max_val1 = num # 최댓값1 
        
    nums.remove(max_val1)  
    
    for num in nums :
        if max_val2 < num :
            max_val2 = num # 최댓값2         
     
    return max_val1 + max_val2 # 두 수의 합 반환



# 테스트 입력
nums = [3, 4, 1, 5, 2] # 0 이상 원소
print('tot =', find_largest_sum(nums))  # tot = 9




# [2] 주어진 리스트에서 중복되지 않는 첫 번째 숫자를 반환하는 함수
'''
  조건> 중복되지 않는 정수가 없을 경우 -1 반환
  예) [2, 3, 2, 4, 3, 5, 2] -> result = 4
'''
def find_first_unique_integer(nums) :
    
    num_set = {} # 빈도수 저장  
    
    # 각 숫자의 등장 횟수 계산    
    for num in nums:  
        if num in num_set:
            num_set[num] += 1
        else:
            num_set[num] = 1    
            
    # 등장 횟수가 1인 첫 번째 정수 반환
    for num in nums:  
        if num_set[num] == 1: 
            return num  
        
    return -1 # 중복되지 않는 정수가 없을 경우 -1 반환

# 테스트 입력
nums = [2, 3, 2, 4, 3, 5, 2]
print('result =', find_first_unique_integer(nums))  # result = 4

nums = [1, 2, 1, 2, 1]
print('result =', find_first_unique_integer(nums)) # result = -1



# [3] 배열에서 중복 단어 제거 후 문자열 반환   
'''
 예) ['이순신', '강호동', '유관순', '강호동']  -> '이순신 강호동 유관순'
'''
def remove_word(names) :
    
    unique_word = [] # 유일단어 저장 
    
    # 중복되지 않은 단어만 추가
    for name in names:
        if name not in unique_word:
            unique_word.append(name)    
    
    return unique_word

# 테스트 입력
names = ['이순신', '강호동', '유관순', '강호동'] 

print('result =', remove_word(names))  



# [4] 배열 회전하기 : 지정한 회전수 만큼 배열의 원소를 반시계반향으로 회전
'''
 예) [1, 2, 3, 4, 5] : 2회전 ->  [4, 5, 1, 2, 3]
'''

lst1 = [1,2,3,4,5]
lst1[0:1]
def rotate_array(arr, k):

    # 회전된 결과 저장
    rotated = arr.copy() # 배열 내용 복제  rotated = [1,2,3,4,5]  
   
    for i in range(k):
        tmp = rotated[:]  # tmp = [1,2,3,4,5]  
        rotated[0] = arr[-(i+1)] # 복제된 배열의 첫번째 원소 # rotated = [5,2,3,4,5]
        
        rotated = rotated[0:1] + tmp[:-1]  #  rotated = [5] tmp = [1,2,3,4]
    
    return rotated


# 테스트 입력 : 배열과 회전 횟수
original_array = [1, 2, 3, 4, 5]

rotation_count = 3

print('result =', rotate_array(original_array, rotation_count)) # result = [4, 5, 1, 2, 3]



# [문제] 다음 배열(nums)에서 가장 높은 빈도수를 찾아서 최빈수와 빈도수를 구하는 함수를 정의하시오. 
''' 
 <출력결과> 최빈수 = 40, 빈도수 = 3
'''

def highest_frequency(nums) :
    
    num_set = {} # 숫자 빈도수 저장 
    
    # 1. 각 숫자의 등장 횟수 계산    
    for i in nums: 
        num_set[i] = num_set.get(i,0) +1
            
    # 2. 최빈수와 빈도수 구하기 
    num = sorted(num_set, key = num_set.get, reverse = True)[0]        
    # 방법2. 
    # num = max(num_set, key = num_set.get)
    freq = num_set[num] #value ★★★★★
    return num, freq  


# 테스트 입력
nums = [10, 40, 50, 10, 40, 30, 40]

num, freq = highest_frequency(nums) # 함수 호출 

print(f'최빈수 = {num}, 빈도수 = {freq}')









