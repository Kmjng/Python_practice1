'''
메서드 재정의(method override)
 - 상속관계에서만 나오는 용어
 - 부모 클래스의 원형 method를 자식에서 다시 작성
 - 인수, 내용 재작성
'''

# 부모 클래스 
class Super :       
    
    # 기본 생성자
    def __init__(self) :
        self.data = 100
    
    # 부모 원형 함수 
    def superFunc(self):
        pass


# 자식1
class Sub1(Super):
    # 기본 생성자 
    
    # 메서드 재정의  
    def superFunc(self):        
        print('자식1 : data = {}'.format(self.data))
    
sub1 = Sub1() # object
sub1.superFunc() # data = 100
    

# 자식2
class Sub2(Super):   
    # 기본 생성자 
    
    # 메서드 재정의  
    def superFunc(self, data):
        self.data = data
        print('자식2 : data = {}'.format(self.data ** 2))

sub2 = Sub2()
sub2.superFunc(200)






