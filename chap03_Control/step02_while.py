'''
반복문(while)

형식)
while 조건 :
    실행문
    실행문 
'''

# 1. 카운터와 누적 변수 
cnt = tot = 0 # 초기화

while cnt < 5 : 
    cnt += 1  # 카운터 변수
    tot += cnt #  누적 변수
    print('cnt=%d, tot =%d'%(cnt, tot))

print(cnt, tot) 
print() # line skip


# 2. 1 ~ n까지 수열 누적합
cnt = tot = 0

while cnt < 100 : # 100회 반복
    cnt += 1 # 카운터
    # tot += cnt # 누적 합
    if cnt%5 == 0 :
        tot += cnt # 5의 배수일 때만 누적합 
    
                
print('1 ~ 100까지 5의 배수 합 = {0:3,d}'.format(tot))   

        
# 3. 무한 루프 : 무한 반복문
# ★★★ 사용 시, 탈출 조건을 넣어준다. ★★★
while True :
    num = int(input('숫자 입력 : '))
    
    if num % 10 == 0 : # ★★★ exit 조건 ★★★★
        print('프로그램 종료')
        break # loop exit     
    print('입력 값 -> ', num)


# 컴퓨터 난수 생성 module ★★★
# C: anaconda3 파일에 라이브러리에 있는 모듈임.
import random

# 모듈제공 함수 확인 
dir(random)

# random 모듈 중 random() 함수는 0~1사이의 난수 생성

# 난수 0.01 미만이면 종료 후 난수 갯수 출력 
cnt = 0 
while True :
    r = random.random() # 모듈명.함수명() ★★★
    print(random.random())
    if r < 0.01 :
        break
    else :
        cnt += 1
print('총 난수 개수:',cnt)  
#0.01 미만 값 나오기 전까지 몇 개의 난수가 나왔는지 확인 

    
# 4. continue, break
# 공통점 : 반복문 에서만 사용하는 명령문이다. 
# break : 반복 탈출 
# continue : 다음 명령문을 수행하지 않고, 반복문 시작으로 간다.
# ★★★ continue 는 특정 조건을 스킵하고 싶을 때 ★★★
# pass : 블록에 마땅히 쓸 명령어가 없을 때 
i = 0
while i < 10 :
    i += 1 # 카운터
    if i == 3 : 
        continue #  다음 문장 skip (시작으로 간다)
    if i == 6 : # 2차 작성  
        break #  루프 탈출(loop exit)
    print(i, end = ' ') 


# randint() 함수 사용해보자 
# 정수형 난수 생성기 
import random 
r = random.randint() # 오류 - 난수 범위가 필요하다. 
r = random.randint(1,10) # 1~10 사이의 정수 범위

while True : 
    r = random.randint(1,10) 
    print('r=',r)
    if r == 6 :
        break
'''
QUIZ

mynum == computer(난수) : '맞추기 성공' -> exit 
mynum > computer(난수) : '더 작은수 입력하세요'
mynum < computer(난수) : '더 큰 수 입력하세요'
단, 난수의 범위는 1~10 이다. 
'''

import random 
computer=random.randint(1,10)
while True : 
    mynum = int(input('값을 입력하세요:'))
    if mynum == computer: 
        print('맞추기 성공')
        break 
    elif mynum > computer:
        print('더 작은수 입력하세요.')
    elif mynum < computer:
        print('더 큰 수 입력하세요.')
    