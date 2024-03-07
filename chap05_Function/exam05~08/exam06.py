# -*- coding: utf-8 -*-
"""
문6) 다음 blood 변수는 8명의 혈액형 정보를 갖는 범주형 변수이다. lambda 함수를 이용하여 
    이 변수의 값을 10진수로 인코딩하는데 만약 map_data에 없는 혈액형은 -1값으로 표시하시오.
   (혈액형과 10진수 관계 : A : 0, B : 1, O : 2 AB : 3 )   
    
    <출력 결과>
    digit = [2, 1, 0, 3, -1, 2, 0, -1]
"""

# mapping table : 혈액형과 10진수 관계 
map_data = {'A':0, 'B':1, 'O':2, 'AB':3} # dict table 


# 혈액형 입력 자료  
blood = ['O','B','A','AB','C','O','A','BA']


digit = None 


# ★★★★★★★★★★★
# 방법 1 
enc = lambda lst, dic: [dic[i] if i in dic.keys() else -1 for i in lst]

print(enc(blood, map_data))

# 방법 2 
enc2 = (lambda lst, dic: [dic[i] if i in dic.keys() else -1 for i in lst] )(blood, map_data)
print(enc2)

# 방법 3
enc3 = (lambda lst : [map_data[i] if i in map_data.keys() else -1 for i in lst] )(blood)
print(enc3)

# 방법 4
digit = [(lambda b : map_data[b])(b) if b in map_data else -1 
                                              for b in blood] 


# test 답틀림/./..
enc2 = lambda lst, dic : [k if i in j else -1 for i in lst for j,k in dic.items()]
print(enc2(blood, map_data))
# for j,k in dic.items() 에 대해 돌리기 때문에 틀림
for i in blood: 
    for j, k in map_data.items():
        if i in j :
            print(j, ":", k)
        else: 
            print(j, ":", '-1')