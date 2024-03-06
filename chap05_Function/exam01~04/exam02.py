'''
문2) 다음 벡터(emp)는 '입사년도 이름 급여'순으로 사원의 정보가 기록된 데이터 있다.
      이 벡터 데이터를 이용하여 사원의 이름만 추출하는 함수를 정의하시오. 

     <출력 결과>
 names = ['홍길동', '이순신', '유관순']
'''


# list 자료 
emp = ["2014 홍길동 220", "2002 이순신 300", "2010 유관순 260"]
s=[]
for i in emp:
    s.append(i.split(sep=' '))


print(s)
# 함수 정의

def name_pro(emp): 
    names = [] # 이름 저장 
    for i in emp:
        s = i.split(sep=' ') #split돼서 리스트화됨 ★★★
        # print(s)
        names.append(s[1])
    return names


# 함수 호출 
names = name_pro(emp) # 주소호출 방식  
print('names =', names)


print(id(emp)) # >> 2300861254080
print(id(names))


# 방법2 ) 
def name_pro(emp): 
    names = [] # 이름 저장 
    names = [i.split(sep=' ')[1] for i in emp ]
    return names
