# -*- coding: utf-8 -*-
"""
문5) 다음 input_data는 A,B,C 세가지 값을 갖는 범주형 변수이다. lambda 함수를 이용하여 
   이 변수의 값을 2진수로 인코딩하시오.
    
    <출력 결과>
    encoding = [[1, 0, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 1, 0]]
"""



# mapping table 
map_data = {'A': [1,0,0], 'B': [0,1,0], 'C' : [0,0,1]}


# 범주형 자료 입력 
input_data = ['A','C','A','B','C','B']

# ★★★★★★★★★★★


lst =[]
for i in input_data:
    for j, k in map_data.items():
        if i in j:
            lst.append(k)

print(lst)

#답 1

def enc(dic, lst):
    a =[]    
    for i in lst:
        for j, k in dic.items():
            if i in j:
                a.append(k)
    return a

print('encoding =', enc(map_data, input_data))

# 답 2 
def enc1(dic, lst): 
    a = [dic[i] for i in lst]
    return a 

print('encoding =', enc1(map_data, input_data))

# 답 3 
def encod(dic, lst):
    a = [ dic[i] for i in lst ] 
    return a
print('encoding =',encod(map_data, input_data))


# 틀린 예 시 

def encod(dic, lst):
    for i in lst:
        a = [dic.values() if i in dic.keys() else pass] 
        # 틀림 리스트내포는 포문이 들어가야함 
    return a
