'''
사람(Person) 클래스 이용 2명의 사람 만들기 

'''

# 부모 클래스(사람) 
class Person :    
    
    # 생성자 : 동적멤버변수   
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
        
    # 멤버메서드 (인스턴스 메소드)
    def info(self):
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}')
        
     
# 자식1 클래스(홍길동)
class Hong(Person): # 클래스 상속        
    pass # 내용 없음   
    
      
# 자식2 클래스(유관순)   
class Yoo(Person): # 클래스 상속  
     
    def __init__(self,name, age, gender, job): # 직업 맴버변수 추가    
        super().__init__(name, age, gender) # 부모의 생성자 호출 super()    
        self.job =job
    
    def info(self): # 맴버변수(self.job) 추가하면서 함수 재정의
        print(f'이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}, 직업: {self.job}')
        
hong = Hong('홍길동',35, '남') #부모의 [생성자]를 호출해 자식클래스 객체 생성
dir(hong)
'''
.... 'age',
 'gender',
 'info',
 'name']
'''
hong.info() # [상속]받는 메소드
# >> 이름 : 홍길동, 나이 : 35, 성별 : 남

yoo = Yoo("유관순",25,'여','회사원')
yoo.info() # >> 이름 : 유관순, 나이 : 25, 성별 : 여, 직업: 회사원
