'''
제어문 (조건문, 반복문)
콜론과 들여쓰기가 중요하다. 
들여쓰기: tab
내어쓰기: shift tab
형식1)
if 조건 :
    실행문
'''

var = 10 # 초기화 
if var >= 5 :
    print('var=', var)
print('var는 5보다 크다.')


'''
형식2) 
if 조건 :
    실행문1 : 조건 True
else :
    실행문2 : 조건 False 
'''

var = int(input('var 변수에 값 입력 : ')) # 키보드 입력 

if var >= 5 :
    print('var는 5이상')
else :
    print('var는 5미만')

# 키보드 입력값 홀짝 판단하기 

var2 = int(input('변수값 입력 :'))

if var2%2 == 0 :        #우선순위: 산술연산자 > 비교연산자> 논리연산자
    print('%d 는 짝수이다'%(var2))
else : 
    print('%d 는 홀수이다.'%(var2))


'''
형식3) if ~ elif ~ else 
if 조건식1 :
    실행문1 -> 조건식1 True
elif 조건식2 :
    실행문2 -> 조건식2 True
else :
    실행문3 -> 모든 조건 False
'''


'''
성적에 대한 등급 구하기
 예) 점수 : 100~90 : 'A학점', 89~80 : 'B학점', 79~70 : 'C학점', 69미만 : '재수강'
''' 

score = 86 # 점수 

# 중첩 if ~ else 
if score < 0 or score > 100 : 
      print('점수 잘못 입력')
else :
    if score >= 90 :
        print('A학점')
    elif score >= 80 :
        print('B학점')
    elif score >= 70 :
        print('C학점')
    else :
        print('재수강')

# 블록 if vs 한줄 if ★★★★ 
# 파이썬은 한줄로 코딩해서 생산성 높이는 것을 선호한다.
'''
변수 = 참 if 조건식 else 거짓
'''

num =9
result = num*2 if num >=5 else num+2 
print(result)
