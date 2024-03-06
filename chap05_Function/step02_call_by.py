# -*- coding: utf-8 -*-
"""
함수 호출 방식
1. call by value : 값으로 호출 
    함수의 인수에 값이 아닌, 변수(값이 들어간 주소)를 넣으면 
    참조변수가 된다. -> call by reference 
2. call by reference : 주소로 호출 
"""

# 디폴트 인수 
def greet(name, msg = '별일없지?'): # 초기값을 갖는 매개변수 
    print(f'안녕, {name}아. {msg}')

greet('김민정')
greet('김민정','뭐하니?')





# 1. call by value   # 값으로 함수 호출 
def modify1(value) :
    lst = [100, 200]  
    lst.append(value) # list 추가 
    print(lst)


# 함수 호출 
modify1(5)  # 값 전달 



# 2. call by reference ★★★ # 주소를 이용해서 함수 호출
# (참조변수)
# 특정 변수의 주소에 접근 가능하다. 

def modify2(lst): # 바깥 변수를 참조한다. 주소를 참조해서 함수를 수행한다. 
    print(id(lst)) # (1)
    lst += [100, 200] # (2) lst = lst + [100, 200]

lst = [1, 2, 3, 4, 5] # 참조 변수 
print(id(lst)) # lst변수가 갖고 있는 주소: 2300914468672
# 이 주소를 그대로 modify2() 함수에 전달한다. 
# 그 주소에 함수내용을 적용한 내용을 반영한다. 

# 함수 호출 
modify2(lst) # >> (1) 2300914468672 & (2) 함수 내용 수행
print(lst) # >> [1, 2, 3, 4, 5, 100, 200]


# 주소 호출 예) list 원소의 평균 구하기    
def modify_list(lst) :
    tot = sum(lst)
    avg = tot / len(lst)
    return avg


my_list = [10, 25, 13, 40, 5] # 이거 다시 실행하면 주소값 바뀐다..
print(id(my_list)) # >> 2300915371584

modify_list(my_list) # >> 18.6 
print(my_list)




















