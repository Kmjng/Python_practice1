'''
    연산자(Operator)
    1. 할당연산자 : 변수에 값 할당
    2. 패킹 할당 : 묶음 할당
    3. 연산자 : 산술, 관계/비교, 
'''
# 1. 할당연산자(=)
i = tot = 10 # 변수초기화 (두 변수에 같은 값 할당) ★★★
i , tot = 10 # 오류 ★★★
print(i, tot) # 10 10
i += 1 # i = i + 1 
tot += i # tot = tot + i  
print(i, tot) 

# 서로 다른값 할당  ★★★
v1, v2 = 100, 200
print(v1, v2)

# 변수 값 교체 ★★★
v2, v1 = v1, v2
print(v1, v2)
'''
tmp = v1
v1 = v2
v2 = tmp
'''

# 2. 패킹 * (packing) 할당 ★★★
v1 =10 #단일변수 
lst = [1,2,3,4,5]  # <-> 단일변수

print(lst) # [1, 2, 3, 4, 5]

v1, *v2 = lst  # 리스트의 상수 하나 v1에, 나머지 리스트 패킹해서 v2로 할당
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5

# ★★★★★★★★★ -민정
num =1,2,3,4,5
print(num) # 튜플로 출력된다. (1,2,3,4,5)
 
a,b,c,d,e = num # a,b,c,d,e 변수에 num 
print(a)
print(c)
# a,b,c,d = num 은 오류(변수 갯수 맞아야함)
a,b,*rest = num 
print(a,b,rest)

# 예시 
def add_profile(name, age, height, weight):
    return f'이름: {name}, 나이: {age}, 키: {height}, 몸무게: {weight}'

person1 = 'KMJ',29,180,45
add_profile(*person1)

# ★★★★★★★★★


# 3. 연산자 : 산술,관계,논리 연산자 
num1 = 100 
num2 = 6

# 1) 산술연산자 
add = num1 + num2
print('add=', add) # add= 106

sub = num1 - num2
print('sub =', sub) # sub = 90

div = num1 / num2 
print('div =', div) # div = 16.666666

div = num1 // num2 
print('div =', div) # div = 16

div2 = num1 % num2
print('div2=', div2) # div2= 0

mul = num1 * num2
print('mul=', mul) # mul= 1000

square = num1 ** 2
print('square=', square) # square= 10000


# 2) 관계 연산자 
# (1) 동등비교 - 숫자형, 문자형, 논리형 
result = num1 == num2  
# num1 == num2 이면 True
# num1 != num2 이면 False 
print(result) # False

result = num1 != num2
print(result) # True

# (2) 크기비교 - 숫자형
result = num1 > num2
print(result)

result = num1 >= num2
print(result)

result = num1 < num2
print(result)

result = num1 <= num2
print(result)

# 3) 논리 연산자 
result = num1 >= 50 and num2 <= 20 # 논리곱
print(result) # True

result = num1 < 50 or num2 <= 20 # 논리합
print(result) # True

result = not(num1 < 50)  # 부정 
print(result) # True







