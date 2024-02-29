
"""
2. 문자열과 문자열 처리 

- 문자열은 상수이다. 문자상수
- 문자열은 순서 또한 저장한다. 

- 문자열 안에 따옴표를 쓰고 싶을 때에는 
문자열'' 안에 "" 큰따옴표로 / 문자열"" 안에 '' 작은따옴표로
또는, \을 앞에 써서 기능을 잃게 할 수 있다. ★★★

- 여러줄의 문자열 ''' 내용 '''  

- 다른 자료형끼리의 + 은 불가능하므로, "student"+str(26) 처럼 해준다. 
- 문자열의 반복을 위해 * 연산자 사용 가능하다. "student"*3

- 문자열은 시퀀스 자료형으로 인덱스가 있고, 인덱스로 값의 접근이 가능하다. ★★★

"""


# 1. 문자열 유형 

# 1) 한 줄 문자열 
lineStr = "this is one line string" 

# 2) 여러줄 문자열 
multiLine = """This
is multi line
string"""

multiLine2 = 'This \nis multi line \nstring' #줄바꿈기호 \n 사용 
print(multiLine2)

# 3) sql문 예시
query ="""select * from emp
where deptno = 1001
order by sal desc"""
print(query)
print(query, type(query))
print('문자열의 문자개수:', len(query))

# 2. indexing/slicing 가능 
'''
색인(index) : 문자열 내 문자들의 순서 (0 ~ n-1)
형식) 변수명[n] or 변수명[-n]
        변수명[start:stop-1:step]
'''
asdf = 'abcdefghijk'
print(asdf[1:5])


# 1) indexing
# 왼쪽 기준 색인 
print('왼쪽의 첫번째 문자 : ', lineStr[0]) 
print(lineStr[0:4]) # 주의: [start:end-1] start 0 , end 3 

# 오른쪽 기준 색인 
print(lineStr[-1]) 
print(lineStr[-6:]) #-6부터 끝까지 

# 2) slicing : 부분문자열 
subStr = lineStr[:4] # 처음부터 4개
print(subStr) # this

lineStr[:] # 전체문자열 
lineStr[::2] #홀수번째 문자 추출
lineStr[::-1] #오른쪽 기준으로 역순 배열 
lineStr[:4] #처음부터 3까지 
lineStr[4:] #4부터 마지막


# 3. 문자열 연산 
print('python' + ' program') # 결합연산자 
print('python ' + 'ver.'+str(3.11)) 
#★★★ Algorithm : str()변환 > 결합(반복)연산자 ★★★

print('-'*50) # 반복연산자 


# 4. 문자열 처리 함수 
'''
함수 vs 매서드 
공통점: 기능을 한다. 
차이점: 
    함수는 단독호출이 가능하다. 
    매서드는 객체를 통해 호출된다. (객체의존적)
    
    함수예시
    sum(iterable) ★★★iterable: 반복가능한 객체
    sum([1,2,3,4,5]) #가능

주의 : count()는 매서드이다. 
    ex. 'oooyyy'.count('y') 
        >>> 3 
'''


testStr = "my name is hong!!"  
testStr = str("my name is hong!!") #동일

# 형식) ★★★ 문자열객체.메서드() ★★★
testStr.count('n')
testStr.capitalize() # 매서드 기능을 객체에 반영해서 반환해줌
# 어떤 함수를 쓸 수 있는 지 함수 목록확인하는 함수 
dir(testStr)

'''
find()
count()
isalpha() 등등
upper() 
replace(,)
startswith() - 시작단어 
'''


print(type(testStr))
# >> <class str>  -- 해석: testStr는 클래스 str에서 만든 객체이다. 
'''
class: 객체 생성 역할 
object: 클래스에 의해서 생성된 결과물
'''
# 1) 문자 찾기 # 인덱스값 반환 ★★★
testStr.find('z') # -1
testStr.find('m') # 0 #최초 발견 위치 반환
testStr.find('h') # 11

# 2) 문자 개수 반환  
testStr.count('n') 

# 3) 문자 유형 여부  # True/False 반환
testStr.isalpha() # False  #공백, 특수문자까지 검사함
testStr.isascii() # True  #아스키문자
testStr.islower() # True 


testStr2 =" hello python!!" 

# 4) 공백제거 & 문자열 시작 대문자 변환 

print(testStr2)
print(len(testStr2))
result = testStr2.strip() # 공백제거 (★ 문자열 처음과 끝 공백만 제거..)
print(len(result))
print(result)


result.capitalize() # 문자열 시작 대문자 변환 
print(result.capitalize())

# 5) 대소문 처리 
result.upper() # 전부변경
result.lower() 


# 6) 접두어 판단 # True/False 반환
result.startswith('he') 
result.startswith('He') 


# 7) 단어 교체  
# 기본적으로 ★전부변경
result.replace('!', '')
result.replace(' ', '') 

asdf = 'abcdxxxfzzzzz'
print(asdf.replace('z',''))
print(asdf.replace('x','e'))

# 특정 개수만 변경하고 싶을 때
print(asdf.replace('x','e',2))

# 5. 문자열 분리(split) & 결합(join)

'''
split(sep=구분자) : 문장(str)을 단어(str)로 
'결합기준구분자'.join(단어들) : 단어,토큰(str)들을 문장(str)으로 
'''
# 5.1. 문자열 분리(split)
print(multiLine)
print(len(multiLine))  #문장길이 : 25 반환
print(multiLine.split('.')) # 문자열 내에 .이 없으므로 구분하지 않고 반환됨.

print(multiLine.split('\n')) # 줄 단위로 문자열 분리
print(multiLine.split(sep='\n')) # 위와 동일
multiLine2 = multiLine.split('\n')
print(len(multiLine2))  
#split되어 저장된 리스트의 길이는 요소 갯수 반환 : 3

# 5.2. 문자열 결합(join)

sepWord = ['This ','is ','multi line string']

print('-'.join(sepWord))
