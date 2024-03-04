'''
반복문(for)

형식) 
for 변수 in 반복가능객체(iterable) :
    실행문
    실행문

★★★ 
반복가능객체(iterable) 
문자열(string), list, tuple, set, dict ★★★★
여기서 변수는 반복가능객체의 원소를 저장하는 역할을 한다. 
'''


# 1. 문자열 객체
string = "나는 홍길동 입니다."
len(string) # 원소 길이 반환 ★★★

# 문자 -> 변수 넘김
cnt = 0
for s in string :
    print(s, end = '') 
    cnt += 1
print(cnt)


# 2. list 객체 : 1차원 벡터 생성 
lst = [1, 2, 3, 4, 5]  
for i in lst:
    print('원소 : ', i)

lst2 = []
for num in lst: 
    print('원소: ',num)
    print('원소*0.5: ',num*0.5)
    if num%2 != 0 :
        lst2.append(num) # 홀수 num 리스트2에 저장 ★★★★
print(lst2)
    

# 3. range 객체 : 순서 있는 정수 생성   
num1 = range(10)  # 0 ~ 9까지 
help(list)

print(num1) # >> range(0,10)
list(num1) # <=> list(range(10))
'''
range() 함수는 파이썬에서 연속된 정수를 생성하고, list()는 그 결과를 리스트로 변환
'''

num2 = range(1, 10)
print('num2 : ', num2)  # range(1, 10)


# range() 숫자배열 확인하는 방법 두가지 
# (1)
print(list(range(1,10)))
# (2) 
for num in range(1,10):
    print(num, end=',')


# 4. list + range 객체    
num2 = range(1, 5)  
print('num2 : ', num2)  

num2 = list(num2) # ★★★ list형 변환 ★★★
print(num2)  # >> [1, 2, 3, 4]
# range()로 만들어진 정수의 배열을 리스트에 넣어준다. 
list(range(1,11,2))

# 1~100 정수 배열 만들기 
dataset = range(1,101)
print(list(dataset))

type(dataset) # >> range type
type(list(dataset)) # >> list type
result = [] #빈 list 

for i in dataset :
    print(i)
for i in list(dataset) : # >> 결과 같음 
    print(i)


# choices()함수 사용해보기 
import random 
dir(random)

random.choices()
help(random.choices)
# choices(population, k=1) #pop: 모집단, k: 표본 개수
sample = random.choices(dataset,k=10)
print(sample)


# 5. 중첩 반복문 (if, while, for 모두 중첩가능)
'''
for i in 열거형객체 :
   for j in 열거형객체 :
      실행문
'''

# 구구단 출력 : range() 함수 이용
# 2단~9단 
for i in range(2, 10):    
    print('~~~ {}단 ~~~'.format(i))
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j))
        
# 2. 문장 -> 문장 OR 단어 추출 
# split() 메소드 사용해서 문자열을 특정적으로 쪼개서 리스트화
string ="""우리나라
대한민국
나는 홍길동 입니다."""
for i in string.split(sep='\n') : 
    print('token:',i)

# 문단 -> 문장, 단어 

sent =[]
words=[]
# 문단 -> 문장
print('---------')
for i in string.split(sep='\n'):
    print('문장:', i)
    sent.append(i)
    # 문장 -> 단어
    for j in i.split(sep=' '):
        print('단어:',j)
        words.append(j)

print(sent)
print(words)
        

# words 리스트 목록의 단어 찾기 
# 단어: ['우리나라','대한민국','나는','홍길동']
print('단어길이:',len(words))
print('3번째 원소:', words[2])
search = input('조회단어: ') 
if search in words : 
    print('검색단어 있음')
else : 
    print('검색단어 없음')