"""
1. 표준 입출력 함수  
"""

help(print) #도움말

# 1. print() 
# - 콘솔 출력 함수 

# 1) 기본 인수 
print("value =",10,10+20)  #문자상수, 숫자상수, 식
#print 내 각 값의 구분으로 한 칸의 공백 
print('010','1234','1111', sep='-') # sep 속성으로 구분자 설정
 
# end 속성 
# end = '\n' # 끝에 줄바꿈 
print('value =', 10, end=',' )
print('value =', 20) # value = 10,value = 20

# 2) % 양식문자 (포멧 지시자 %d, %s) ★★★
# 문자열안에서 해석된다. 
# 형식) print('%양식문자' %값) - ppt.3

num1 = 10; num2 = 20
tot = num1 + num2 
print('%d + %d = %d' %(num1, num2, tot)) 

print('이름은 %s이고, 나이는 %d 이다.' %('홍길동', 35)) 

print('원주율 = %8.3f' %(3.14159)) 

# 50% 비율을 출력하고 싶을 때 %% 라고 기입해준다. ★★★
print('전체 찬성률은 %d%%이다.'%50) 
title ='분류정확도는 %.5f 이다.'
acc= 145/150
print(title%acc) # ★★★

# 3) format()함수 이용 
# '...{}...'.format(값1, 값2, ...) 
# [1] 순서 기반 포멧 ★★★
print('이름은 {}이고, 나이는 {}이다.'.format('홍길동', 35))
# >> 이름은 홍길동이고 나이는 35이다.
print('이름은 {0}이고, 나이는 {1}이다.'.format('홍길동', 35))
# >> 이름은 홍길동이고 나이는 35이다.
print('이름은 {1}이고, 나이는 {0}이다.'.format('홍길동', 35))
# >> 이름은 35이고 나이는 홍길동이다.

# [2] 순서와 양식 포멧 : {순서:포멧}   ★★★
# ex. {1:5d} %5d 다섯자리 정수로/ (2:3,d) %3,d 정수 3자리마다 콤마
print('정수형 = {0}, {1:5d}, 연봉 : {2:3,d}'.format(123, 1234, 2500))
print('원주율 = {0:.3f}, {1:8.3f}'.format(3.14159, 3.14159))

# [3] format(값, '양식') ★★★
print('원주율 = ', format(3.14159, '5.3f'))

# 20번 부서번호 조회 
deptno = 10 
sql = 'SELECT * FROM emp WHERE deptno = {}'.format(deptno)
print(sql)

deptno = input('부서번호 입력:') #부서번호 
sql = 'SELECT * FROM emp WHERE deptno = {0}'.format(deptno)
print(sql)

# [4] 축약된 format  ★★★★★★
sql = f'SELECT * FROM emp WHERE deptno = {deptno}'
print(sql)

# 2. input()
# - 키보드로 입력받는 함수 
# ★★★ 숫자를 input 해도 항상 문자열로 저장되기 때문에 정수형으로 변환해줘야 한다.

# 키보드 입력 -> 정수형 변환 
a = int(input('첫번째 숫자 입력 : ')) # 10
b = int(input('두번째 숫자 입력 : ')) # 20

c = a + b
print('c=', c) # c= 30


# 3. 자료형 변환 
# - 현재 자료형을 다른 자료형으로 변환 
'''
int() : 정수형 변환 / 소수점 절사 
float() : 실수형 변환
str() : 문자형 변환
bool() : 논리형 변환 /   
'''
print(bool(1)) # True 
print(bool(0))  # False 
print(bool(3))  # True 
help(bool)






