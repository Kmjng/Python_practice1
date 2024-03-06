'''
step04 + step05 문제 

 문1) 중복 되지 않은 직위와 각 직위별 빈도수를 출력하시오.
 
 <<출력 결과 >>
 중복되지 않은 직위 : ['사장', '과장', '대리', '부장'] - set()
 각 직위별 빈도수 : {'과장': 2, '부장': 1, '대리': 2, '사장': 1} 
'''

position = ['과장', '부장', '대리', '사장', '대리', '과장'] # list 

print(set(position))

print(type(position)) # class 'list'

cnt ={}
for i in position : 
    cnt[i] = cnt.get(i,0) +1 
    # cnt 딕트에 i 라는 key를 넣고 = value 삽입

print(cnt)