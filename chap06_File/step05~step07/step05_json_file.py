# step05_json_file.py
# step06_json_file.py
'''
json 파일 (str type★)
 - 네트워크상에서 표준으로 사용되는 텍스트 파일
 - 파일 형식 : {key:value, key:value} # ★ key value 로 구성
 - 활용 예 : 서로 다른 플랫폼(java vs python)에서 파일 공유
      json 파일 : [자바 웹 페이지] 구현을 [파이썬 딕셔너리] 형태로~


- json 모듈 기능 
 1. encoding : Python 객체 -> json file 저장 (파일 출력★)
 2. decoding : json file 읽기 -> Python 객체 변환 (파일 입력★)
  << ★★ 목적이 json파일이니까 파이썬에서 decoding(해석)하고 작업한다고 해석하자..
 
[{key1:value1, ...},{key1:value1, ...}] : 배열 (Array) 타입 
{key1:value1, ...},{key1:value1, ...} : 객체(Object) 타입 

str - json - encoding - dumps(dict객체)/ dump(dict객체, 파일객체)
dict - python - decoding - loads(string객체)/load(list객체)

'''


import json # json파일 입출력을 위한 모듈

dir(json)
'''
dumps() : json file 저장(인코딩)  ★★★★
loads() : json file 읽기(중괄호 디코딩) - 해독 ★★★★
load() : json file 읽기 (대괄호 디코딩) ★★★★
'''
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'

##########################
### 1. json encoding
##########################

# 1) python dict 
user = { 'eno': 1234,  'ename': '홍길동', 'job':'관리자'} 

# 2) json 인코딩 부터 한다. : python dict 에서 json 문자열 객체로 ★★★★
json_encoding = json.dumps(user, ensure_ascii=False) # ASCII 인코딩 안함 (한글을 그대로)
 # ASCII 인코딩하면 어케되징?
print(json_encoding) 
type(json_encoding) #>> class 'str' 

# 3) json file 저장  
file = open(path + "/json_data.txt", mode='w', encoding='utf-8') # 작성 (write)목적으로 연다(open)
file.write(json_encoding)
file.close()



##########################
### 2. json decoding 
##########################

# 1) json file 읽기 ( readline()으로 읽기 )
file = open(path + "/json_data.txt", mode='r', encoding='utf-8')
json_data = file.readline() # 읽어오니까 그대로 str임. 그리고 readline()이니까 str
file.close()

print(json_data)  # {'eno': 1234, 'ename': '홍길동', 'job': '관리자'}
type(json_data)  
# >> class 'str' 
# 따라서 json_data['ename'] >> 오류 

# 2) json  디코딩 : json 문자열 -> python dict ★★★★
python_dict = json.loads(json_data) #파일이 열린 상태에서 해야하나?????
python_dict['ename'] # >> '홍길동'


# 3) python dict 
print(python_dict) # {'eno': 1234, 'ename': '홍길동', 'job': '관리자'}
type(python_dict)  #>> class 'dict' 



#############################
### 3. json file 읽기 (1)   # usagov_bitly.txt 파일로 실습 -> 객체{} 로 구성된 json 파일
#############################

# (텍스트파일이어도 내용물이 json이면 json파일이라고도 한다.)

# 1) json file 읽기 
file = open(path + "/usagov_bitly.txt", mode='r', encoding='utf-8')


# 일단 형식이 txt니까 다음과 같이 실행 가능하다. 
lines = file.readlines() # 줄단위 전체 읽기(list 반환)
file.close()
print(lines)
len(lines) # >> 3560

type(lines) # >> class 'list'
type(lines[0]) # class 'str' >> json 문자열

# 2) json  디코딩해서 list에 저장해보자 : 줄 단위 텍스트 읽기 -> json 문자열  -> list 저장 
py_obj = [] # json 문자열 하나씩 받아서 python dict로 저장하겠다. (단, 전체는 list)

for line in lines :
    py_obj.append(json.loads(line)) # json 디코딩 (dict로 변환해서 리스트에 append한다.)

# 디코딩 방법 2 - list comprehension 
py_obj2 = [json.loads(i) for i in lines]

py_obj
# 첫번째 원소  
print(py_obj[0])
type(py_obj[0]) # class 'dict' >> python 사전형
type(py_obj) # class 'list' 
py_obj[0]['u'] # 'u'라는 key의 value 검색 

# 디코딩한 내용 출력해보기
for i in py_obj[:5] :  # dict에서 다섯 줄 (0~4)
    print(i) 
    print(type(i))


urls = [] 
for i in py_obj: # dict
    try:     
        urls.append(i['u']) #value append 
    except: 
        print('u키가 없습니다.')
urls
len(urls) #>> 3440 # 3560 중 120개는 key가 없다. 


#############################
### 3. json file 읽기 (2)   # labels.json 파일로 실습 -> 배열[] 로 구성된 json 파일
#############################

# 1) json file 읽기  (대괄호 형식) [{},{},{}...]
file2 = open(path + "/labels.json", mode='r', encoding='utf-8') 

# 형식이 json이니까 일단 디코딩 부터 한다. 
result2 = json.load(file2) # 디코딩
type(result2) # >> class 'list'
print(len(result2)) # 30 


# 디코딩 확인 - key 값으로 value 검색해보기 
result2[0]['url'] # >> 'https://api.github.com/repos/pandas-dev/pandas/labels/Bug'
type(result2) # >> class 'list'
print(result2)




'''
2. json file 쓰기(저장)
dumps vs dump
dumps(object) : json 문자열 변환(encoding) -> json 파일 저장 (객체 형식) 
dump(object, file) : json 문자열 변환(encoding) & json 파일 저장(배열 형식) 
'''    

result2 # list 객체 
type(result2)
type(result2[0]) # dict


# 1) 중괄호 형식 저장 - dumps(object) 사용
file1 = open(path + '/json_data1.txt', mode='w')

for row in result2 :
    file1.write(json.dumps(row)+'\n')      


file1.close() # file 닫기 


# 2) 대괄호 형식 저장 
file2 = open(path + '/json_data2.txt', mode='w', encoding='utf-8')
json.dump(result2, file2) # json.dump(object, file)

file2.close()  # file 닫기 


