'''
변수(variable); 자료(값)이 저장된 메모리 이름
형식 : 변수명 = 값 or 수식 or 변수 

F5 : 전체실행 단축키 
F9 : 줄 단위 실행 단축키
'''

# 1. 변수와 자료형 
var1 = "Hello python"
var2 = 'Hello python'
print(var1)
print(var2)

# 주소가 궁금..
print(id(var1),id(var2))


# type() : 변수 자료형 확인  
print(type(var1), type(var2)) # print()에 컴마로 나열해서 여러값을 출력 가능

var1 = 100 # 변수 수정  
print(var1, type(var1)) 

var3 = 123.2345
print(var3, type(var3)) 

var4 = True
print(var4, type(var4)) 


# 2. 변수명 작성 규칙(ppt.21 참고)
'''
- 첫자 : 영문자 or _ 사용가능 
- 두번째 : 숫자 사용 가능 
- 대소문자 구분(Score, score)
- 낙타체 : 두 단어 결합(korScore)
- 명령어, 클래스명, 함수명 사용불가, 한글명 비권장
- 점(.) 사용 불가  
'''

_num = 10
_Num = 20


# 낙타체
korScore = 89
matScore = 75
engScore = 55
sciScore = 54
sciScore2= 54
print(id(korScore), id(matScore), id(engScore),id(sciScore),id(sciScore2))
'''
>> 140728535916072 140728535915624 140728535914984 140728535914952 140728535914952
'''


tot = korScore + matScore + engScore
print('tot =', tot) # tot = 219


# python 명령어 확인할 수 있는 모듈 keyword
# ★★★ python 명령어에 해당하는 워드는 변수명으로 지정할 수 없다. ★★★
import keyword 
kword = keyword.kwlist # 명령어 목록(kwlist) 변수에저장해서 가져오기
print('python명령어 : ',kword)
print('명령어갯수 : ', len(kword))

# 3. 참조변수 : 메모리의 주소를 갖는 변수 
# 메모리에 저장된 값 : 객체 (object)
x = 150 # x는 150의 주소 저장 
x2 = x # x의 주소 복사 ★★★

print(x) # x의 내용 출력 
print(id(x), id(x2)) # x의 주소 출력 
    # >> 140728535918024 140728535918024

#이 때, x2의 값을 변경하면, x2의 주소는 다른 주소로 할당되는 듯 ★★★
x2 = 151 
print(id(x), id(x2))
    # >> 140728535918024 140728535918056
    '''
    주의해야 할 점 : 같은 값을 가졌다고 해서 모두 동일한 object를 가리키는 것은 아니라는 것이다.
    파이썬 특으로, -5 ~256 사이의 숫자들은 미리 메모리에 할당되어 있고, 항상 동일 id 를 가지고 있다.
    
    번외) 
    따라서 두 변수를 비교해야 할 경우, [해당 값을 비교하는 것★ - == 사용]인지 
    아니면 해당 변수가 가리키는 object의 [id를 비교하는 것★ - is 사용]인지 명확히 해야할 필요가 있다. 
    
    Python 에서는 실제 사용하지 않더라도 -5 와 256 사이의 정수들을 integer object 배열에 미리 저장해둔다. 
    이에 따라 해당 숫자를 값으로 할당하려고 할 경우 미리 저장된 object 의 reference 를 참조하도록 한다. 
    
    출처: https://technote.kr/183#fourth [TechNote.kr:티스토리]

    '''

x3 = 500 
x4 = 500
x5 = 501
print(id(x3),id(x4),id(x5))
# >> 1861944611952 1861944611504 1861944611984







