'''
문3) 아래와 같은 중첩함수(ATM)를 클래스로 정의하고 2개의 객체를 생성하시오.
        조건1) 첫번째 객체명 : acc1
        조건2) 두번째 객체명 : acc2
'''

def ATM_df(bal) : # 현금자동 입출금기 
    accBal = bal # 잔액
    
    # 잔액 조회 : 획득자(getter)
    def getBal() :
        return accBal
    
    # 입금하기 : 지정자(setter)
    def deposit(money) :
        nonlocal accBal
        accBal += money
        
    # 출금하기 : 지정자(setter)  
    def withdraw(money) :
        nonlocal accBal
        accBal -= money
        
    return getBal, deposit, withdraw


# 클래스 정의 
class ATM :   
    
    # 생성자 
    def __init__(self, bal) :
        self.accBal = bal # 동적 멤버변수 : 잔액 
    
    # 멤버메서드 
    # 잔액 조회 : 획득자(getter)
    def getBal(self) :
        return self.accBal
    
    # 입금하기 : 지정자(setter)
    def deposit(self, money) :
        self.accBal += money
        
    # 출금하기 : 지정자(setter)  
    def withdraw(self, money) :
        self.accBal -= money

# 첫번째 객체 
acc1 = ATM(1000) 
acc1.getBal() # 1000


# 두번째 객체 
acc2 = ATM(100)
acc2.getBal() # 100











