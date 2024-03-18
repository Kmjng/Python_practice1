'''
정보은닉(Information Hiding)
  - 객체를 통해서 필드로 직접 접근을 차단하고, 획득자(getter)나 지정자(setter) 
    메서드를 통해서만 접근하도록 클래스를 설계하는 기법   
  
예) 은행 계좌 클래스 
   멤버변수 : 잔액(balance)
   멤버메서드 : 잔액확인(획득자), 입금하기(지정자), 출금하기(지정자) 
'''

class Account :    
    # 생성자 : 객체 생성 + 멤버변수 초기화 
    def __init__(self, bal):
        # 동적 정보은닉 멤버변수 
        self.__balance = bal # 잔액 초기화 
            
    # 잔액확인 : 획득자(getter) - return 명령어 
    def getBalance(self): 
        return self.__balance 
    
    # 입금하기 : 지정자(setter) - 매개변수 필요  
    def deposit(self, money):
        self.__balance += money
    
    # 출금하기 : 지정자(setter)  - 매개변수 필요 
    def withdraw(self, money):
        if self.__balance >= money :  
            self.__balance -= money
        else :
            print('잔액이 부족합니다.')
    
    
# object 생성 
acc1 = Account(1000) # 객체 생성 & 잔액 초기화 

dir(acc1)
''' 
 'deposit', : 메서드(입금하기)
 'getBalance', : 메서드(잔액확인) 
 'withdraw' : 메서드(출금하기) 
'''    
acc1.getBalance() # 1000

acc1.deposit(20000) # 2만원 입급 

acc1.getBalance() # 잔액 확인 

acc1.withdraw(5000) # 5천원 인출 

acc1.getBalance() # 잔액 확인














    
    
    
    
    