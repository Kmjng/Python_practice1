'''
함수 장식자 
  - 다른 함수의 시작과 종료부분에 장식을 추가하는 기능 
  - 또 다른 함수이다. 
함수 잠금 역할 (login 함수접근가능 logout 인증없인 접근불가)




(1) 함수장식자 생성 
    def 함수장식자명(함수인자) : 
        def inner():
            print()
            함수()
            print()
    return 클로저
    
(2) 실행 형식 
    @함수장식자명
    def 함수명(): 
        실행문
(3) 함수 실행 
    함수명() 

'''

# 함수 장식자 만들기 ( 중첩함수 이용 )
def hello_deco(func) :  
    def inner() : 
        print('*'*20)
        func()  #함수 호출 
        print('*'*20)
    return inner
    

# 대상 함수에 함수 장식자 적용  
@hello_deco 
def hello() :
    print('my name is 홍길동')


# 함수 호출 
hello() # ★★★ 여기서는 내부함수에 인수를 안받기 때문에 인수를 넣지 않는다. 

# (2) 
# 함수 장식자 만들기 ( 중첩함수 이용 )
def hello_deco(func) :  
    def inner(name) : 
        print('*'*20)
        func(name)  #함수 호출 
        print('*'*20)
    return inner

@hello_deco  #다른 함수에 같은 함수장식자 사용하기
def hello2(name) :  
    print(f'my name is {name}')

hello2('홍길동')


'''
함수장식자 적용 예 
함수 호출 전: 로그인(id= 'hong',pwd = '1234')
함수 호출 : 로그인 성공 
함수 호출 후 : '로그아웃' 또는 '로그인실패'

'''

def author(func):
    def inner(a,b):
        func(a,b)
        if a == 'hong' and b =='1234':
            print('로그인 성공 ')
        else : 
            print('로그인 실패 ')
    
    return inner
       
        
@author 
def user1(id, pwd):
    print(f'~로그인(id ={id}, pwd = {pwd})~')
    return id, pwd

@author 
def user2(id, pwd):
    print(f'~로그인(id ={id}, pwd = {pwd})~')
    return id, pwd

user1('hong','1234')
user2('hooo','3333')

'''
~로그인(id =hong, pwd = 1234)~
로그인 성공 
~로그인(id =hooo, pwd = 3333)~
로그인 실패 
'''