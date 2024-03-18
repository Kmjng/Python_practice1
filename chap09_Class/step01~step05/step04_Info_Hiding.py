'''
정보은닉(Information Hiding)
  - 객체를 통해서 필드로 직접 접근을 차단하고, 획득자(getter)나 지정자(setter) 
    메서드를 통해서만 접근하도록 클래스를 설계하는 기법   
  
예) 은행 계좌 클래스 
   멤버변수 : 잔액(balance)
   멤버메서드 : 잔액확인(획득자), 입금하기(지정자), 출금하기(지정자) 
'''

class Account : 
   
    # 생성자 
    def __init__(self, bal, name, no):
        # 동적 멤버 변수 
        self.balance = bal # 잔액 초기화 
            
    # 잔액확인
    def getBalance(self): 
        return self.balance 
    
    # 입금하기 
    def deposit(self, money):
        self.balance += money
    
    # 출금하기 : setter 
    def withdraw(self, money):
        self.balance -= money
    
    
# object 생성 
acc = Account(1000) # 객체 생성 & 잔액 초기화 









    
    
    
    
    