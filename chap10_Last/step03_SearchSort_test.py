
### 3. 자료구조 : 자료 탐색(search)과 정렬(sort) 


# [1] 선형탐색(Linear Search) 알고리즘 [ppt.15 참고] 
'''
선형탐색 : 배열에서 원하는 값을 찾기 위해 처음부터 끝까지 순차적으로 탐색하는 방법
예) 배열 : [10, 5, 1, 8, 3, 2, 6] -> 찾고자 하는 값: 3 -> index = 4
'''

def linear_search(arr, target):
    
    for idx in range(len(arr)):
        if arr[idx] == target:
            return idx  # 인덱스 반환
    
    return -1  # 찾는값이 없으면 -1 반환


# 데스트 자료 : 배열과 찾을 값   
arr = [10, 5, 1, 8, 3, 2, 6] 
target = 3

# 선형 탐색 수행
idx = linear_search(arr, target)



# [2] 이진탐색(Binary Search) 알고리즘 [ppt.16 참고]
'''
이진탐색 : 배열의 중간에 있는 항목과 찾고자 하는 값을 비교하고, 찾고자 하는 값이 
  만약 중간 값보다 작으면 중간 값의 왼쪽 부분서 탐색을 수행하고, 중간 값보다 크면 
  중간 값의 오른쪽 부분에서 탐색을 수행한다.(자료가 많은 경우 탐색시간 빠름) 
''' 

def binary_search(arr, target):
    start = 0 # 시작 위치 
    end = len(arr) - 1 # 끝 위치 

    while start <= end : 
        mid = (start + end) // 2 # 1. 중간위치(정수값) 선택

        if arr[mid] == target: # 2. 중간값과 찾을 값 비교  
            return mid 
        elif arr[mid] < target: # 3. 중간값 보다 큰 경우  
            start = mid + 1
        else: # 4. 중간값 보다 작은 경우 
            end = mid - 1
        
    return -1 # 찾는 값 없으면 -1 반환 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 56

print('index =', binary_search(arr, target))  # index = 7



# [2] 자료 정렬(sort) : 정렬되지 않은 두 개 리스트를 하나로 합쳐서 정렬하기  

'''
선택정렬 알고리즘 : 가장 작은 값을 선택하여 배열의 맨 앞으로 이동시키는 정렬 알고리즘[ppt.18 참고] 

 배열 : [6, 3, 1, 5, 2, 4]

 <선택정렬 : n-1 회전>  
 [1, 3, 6, 5, 2, 4]
 [1, 2, 6, 5, 3, 4]
 [1, 2, 3, 5, 6, 4]
 [1, 2, 3, 4, 6, 5]
 [1, 2, 3, 4, 5, 6]
'''
# 기준위치에 대한 변수 하나가 더 필요하다.~~~~
def merge_lists(lst1, lst2) :
    merged_lst = lst1 + lst2 # 리스트 결합 
    
    n = len(merged_lst) # 배열 길이 
    
    for i in range(n-1) : # 기준색인
        base = i # 배열 기준위치  
        
        for j in range(i+1, n) : # 비교색인 #선택된i보다 큰녀석들과 비교한다.
            if merged_lst[base] > merged_lst[j] :  
                base = j # 배열 기준위치 변경  
        # 배열의 맨앞쪽에 최소값 이동         
        merged_lst[i], merged_lst[base] = merged_lst[base], merged_lst[i]
        
    return merged_lst
        
# 테스트 입력
lst1 = [6, 3, 1]
lst2 = [5, 2, 4]

print('result =', merge_lists(lst1, lst2)) # result = [1, 2, 3, 4, 5, 6]



# [문제] 배열에서 중복되지 않는 숫자들의 원소와 개수를 찾는 함수를 작성하세요.
'''
예) nums = [1, 2, 3, 2, 4, 3, 5]
   
    중복되지 않은 원소 개수 = 3 
    중복되지 않은 원소 = [1, 4, 5]
'''

def count_unique_numbers(nums):
    
    num_set = {} # 각 숫자의 등장횟수(출현빈도수) 
    
    unique_nums = [] # 중복되지 않는 숫자 원소
    unique_count = 0 # 중복되지 않은 숫자 개수 
    
    
    # 1. 각 숫자의 등장 횟수(출현빈도수) 계산
    for i in nums : 
        num_set[i] = num_set.get(i,0) +1 
    for j,k in num_set.items():
        if k == 1 : # value k 가 1 이면
            unique_nums.append(j) # key j를 append해야함 
            unique_count +=1 
        
    print(num_set)
    
    # 2. 등장 횟수가 1인 숫자와 개수 : 중복되지 않은 숫자의 원소와 개수  
    
    return unique_count, unique_nums


# 테스트 입력
nums = [1, 2, 3, 2, 4, 3, 5]
unique_count, unique_nums = count_unique_numbers(nums)

print('중복되지 않은 원소 개수 =',unique_count) # 중복되지 않은 원소 개수 = 3
print('중복되지 않은 원소 =',unique_nums)  # 중복되지 않은 원소 = [1, 4, 5]





