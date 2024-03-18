'''
문4) 사원(Employee) 클래스에서 정의한 멤버(name, pay, info)를 정규직(Permanent) 클래스와
    임시직(Temporary) 클래스에 각각 상속하여 사원의 이름은 name에 저장하고,
    급여는 아래 <조건>에 맞게 정규직과 임시직의 급여 계산 방식으로 계산하여 pay에 
    저장하시오. 이름과 급여관련 자료는 키보드로 입력받으며 기타 사항은 <출력결과 예시>를 
    참고하세요.
     
     <조건1> 정규직(Permanent) 급여(pay) = 기본급 + 상여금 
     <조건2> 임시직(Temporary) 급여(pay) = 작업시간 * 시급 
     
     <정규직 출력결과 예시>
     직원유형 : 정규직 -> 키보드 입력 
     이름 : 홍길동     -> 키보드 입력 
     기본급 : 2000000  -> 키보드 입력 
     보너스 : 500000   -> 키보드 입력     
     출력결과 : 홍길동, 지급액 : 2,500,000 

     <임시직 출력결과 예시>
     직원유형 : 임시직  -> 키보드 입력 
     이름 : 강호동     -> 키보드 입력 
     작업시간 : 200    -> 키보드 입력 
     시급 : 9000       -> 키보드 입력 
     출력결과 : 강호동, 지급액 :1,800,000     
'''
# 사원 클래스 
class Employee : 
    def __init__(self, name, pay):
        self.name = name 
        self.pay = pay 
    
    def info(self):
        print("이름: {0}, 지급액: {1:3,d}".format(self.name, self.pay))

class Permanent(Employee):
    '''def __init__(self, name, sal, bonus):
        super().name = name 
        self.sal = sal
        self.bonus = bonus '''
    pass

class Temporary(Employee):
    '''def __init__(self, name, time, sal_hour):
        super().name = name 
        self.time = time 
        self.sal_hour = sal_hour'''
    pass


# 키보드 입력 & 객체 생성 
kind = int(input('직원유형(1.정규직, 2.임시직) :'))
# name = input('이름 :')


# 직원유형에 따라서 데이터 입력과 객체 생성  
if kind == 1 : # 정규직
    name = input('이름 입력:')
    sal = int(input("기본급 입력:")) #기본급 입력
    bonus = int(input("보너스 입력:")) #보너스 입력
    person1 = Permanent(name, sal+bonus)
    person1.info()

elif kind == 2 : # 임시직  
    name = input('이름 입력:')
    time = int(input("작업시간 입력:") )
    sal_hour = int(input("시급 입력:") )
    person2 = Temporary(name, time * sal_hour)
    person2.info()
else :
    print('잘못 입력했습니다.')



print(person1.name) # 입력한 이름 나옴 
print(person1.pay) # 입력한 급여 계산돼서 나옴






   
    
