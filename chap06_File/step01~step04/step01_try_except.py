'''
예외처리 예 
  - file/DB 입출력 시 문제 발생 (★★ 여러 파일에 적용하다보면 오류가 발생할 수 있기 때문)
  - 반복 수행 과정에서 계산이 불가능한 자료 포함
  - url을 이용하여 웹문서를 수집할 경우 해당 url이 없는 경우 

예외처리 형식)  
try :
    예외발생 코드 
except 예외처리클래스 as 변수:  # ★★★ 예외처리클래스 : 기본값으로 Exception 이 들어감
    예외처리 코드 
finally :
    항상 실행 코드

# 예외처리 클래스: 오류메세지들에 대한 클래스로 따로 분류되어 있는 듯하다. 

'''



# 1. 반복 수행 과정에서 계산이 불가능한 자료 포함

print('프로그램 시작 !!!')
x = [10, 20, 5, 30, 'num', 7 ]

for i in x :
    try: 
        print(i)    
        y = i**2  # num TypeError : unsupported operand(피연산자)
        print('y =', y)
    except : 
        print('예외발생')

print('프로그램 종료')

# 예외처리 클래스 ★★★★
for i in x :
    try: 
        print(i)    
        y = i**2  
        print('y =', y)
    except Exception as e :  
        print('예외발생:',e) # 문제 원인 알려줌

print('프로그램 종료')


# 2. 유형별 예외처리 ★★★★
try:
    num = int(input("정수를 입력하세요: "))
    result = 10 / num # 분모가 0 인경우 
    print("결과:", result)
    open('text.txt', mode ='r') # 해당 파일이 없으면? Exception 예외처리로 간다. 
except ValueError :  # ex) 2.5 입력
    print("유효한 숫자를 입력하세요.")
except ZeroDivisionError as z:   # ex) 0 입력
    print("0으로 나눌 수 없습니다.", z)
except Exception as e: # 이외 예상치 못하는 오류 처리 (예외사항들 마지막에 온다.)
    print("기타 오류 발생:", e)   
    
# 예외처리 클래스를 찾아보는 방법 help() 함수 

help(Exception)



# 3. 예외처리 : 응용
texts = ["홍길동 사원 10", "이순신 관리자 20", "강호동", "강감찬 이사 30", "유관순 과장 20"]


positions = []
for st in texts :
    try : 
        tokens = st.split(' ') # 토큰화(리스트화)
        positions.append(tokens[1])
    except Exception as e : 
        print("예외발생 :",e) # >> list index out of range
print('positions : ',positions) # positions :  ['사원', '관리자', '이사', '과장']
        



















    
    
    
    
    
    
    