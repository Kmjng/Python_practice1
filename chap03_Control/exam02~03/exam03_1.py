'''
step03 관련 문제

문1) 사원의 정보를 저장한 emp 변수를 대상으로 사원의 이름만 추출하여 names에 저장하시오.

       <출력결과>
       이름 = ['홍길동', '이순신', '강호동']
'''

emp = ['1001,홍길동,사원','1002,이순신,대표','1001,강호동,관리자']
names = []

# ★★★ 카운터 변수를 활용하자 ★★★

for i in emp: #emp 리스트 인덱스 
    cnt= 0 # 카운터 변수가 어디에 있느냐가 중요한듯 ★★★
    for j in i.split(sep=','):
        cnt+=1
        if cnt ==2: #카운터가 2일 때의 원소 반환
            names.append(j)
        
print(names)

# 방법 2
names =[]

for i in emp: #emp 리스트 인덱스 
    token= i.split(sep=',') # '1001','홍길동','사원' 리스트화
    names.append(token[1])


print(names)

# 방법 3?
names =[]
token =[]
for i in emp: #emp 리스트 인덱스 
    token.append(i # '1001','홍길동','사원'
    names.append(token[1])

print(names)