# -*- coding: utf-8 -*-

### 2. 수치 연산 : 수열을 대상으로 연산(피보나치 수열, 팩토리얼 계산) 


# [1] 팩토리얼 계산하기 : 정수 N을 입력받아서 N의 팩토리얼을 계산
'''
 예) n=5 -> 1*2*3*4*5 = 120
'''
def factorial(n) :
    result = 1
    
    for i in range(1, n + 1): 
        result *= i 
    
    return result


# 테스트 입력
n = 5
print('result =',factorial(n))  # result = 120



# [2] 피보나치 수열 출력하기 : 정수 N을 입력받아 N의 피보나치 수열 나열  
'''
피보나치 수열 : 두 개의 항을 더하여 다음 항을 만드는 수열
예) n=8 -> [0, 1, 1, 2, 3, 5, 8]
'''

def fibonacci_numbers(n) :
    fib_nums = [0, 1]  # 피보나치 수열의 배열  
    
    while True:
        next_num = fib_nums[-1] + fib_nums[-2]  # 다음 항 계산 (뒤에 있는 두 숫자 더함)
        
        if next_num > n:  # 반복 중단 조건 
            break
        
        fib_nums.append(next_num)  
        
    return fib_nums

# 테스트 입력
n = 8
print('result =', fibonacci_numbers(n)) # [0, 1, 1, 2, 3, 5, 8]

n = 34
print('result =', fibonacci_numbers(n)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]




# [문제] 다음 주어진 정수 배열(arr)에서 연속된 요소의 합 중 최댓값을 찾는 함수를 작성하세요.
'''
예) arr = [2, -1, 4]
   
    <배열의 첫번째 원소로 두 변수 초기화> 
    현재까지의 서브배열 합(current_sum) = 2
    현재까지의 서브배열 합 중 최댓값(max_sum) = 2

    <1회전 결과> : 배열의 두번째 원소와 서브배열 합 구하기 & 최댓값 찾기 
    현재까지의 서브배열 합(current_sum) = (2 + -1) -> 1
    현재까지의 서브배열 합 중 최댓값(max_sum) = max(2, 1) -> 2

    <2회전 결과> : 배열의 세번째 원소와 서브배열 합 구하기 & 최댓값 찾기 
    현재까지의 서브배열 합(current_sum) = (1 + 4) -> 5
    현재까지의 서브배열 합 중 최댓값(max_sum) = max(2, 5) -> 5
'''

def max_subarray_sum(arr):
    
    # <배열의 첫번째 원소로 두 변수 초기화> 
    current_sum = arr[0]  # 현재까지의 서브배열 합
    max_sum = arr[0]  # 현재까지의 서브배열 합 중 최댓값 
    accum = [2] 
    for num in arr[1:] : # 두번째 원소 이후 부터 서브배열 합 구하기 & 최댓값 찾기 
        current_sum = current_sum + num # 서브배열 합 2-1 = 1 
        accum.append(current_sum) # [2,1]
        max_sum = max(accum) # 2

    return max_sum

# 테스트 자료 
arr = [2, -1, 4, -2, -1, 2, 1, -2, 4]

print('서브 배열의 합 중 최댓값 =', max_subarray_sum(arr))  # 서브 배열의 합 중 최댓값 = 7




