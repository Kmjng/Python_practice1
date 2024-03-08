'''
텍스트 파일 입출력(file input/output)
 - 데이터 입출력 시(file, db) 예외 처리한다.
 형식) open('파일경로/파일명', mode='r'/'w'/'a')
        mode = 'r' : 파일 읽기
        mode = 'w' : 파일 쓰기
        mode = 'a' : 파일 쓰기 + 추가
        
        
모든 파일은 논리적 파일 구조를 가지고 있으며 
모든 텍스트의 끝에는 EOF 로 되어 있다. (End of File)

mode = 
    "r" # 읽기모드 
    "w" # 쓰기모드
    "a" # 추가모드 (append)
    "r+" # 읽기와 쓰기 모드 

'''

# 방법 1

# 파일 경로 (를 지정해주면 따로 os 모듈 임포트 해주지 않아도 된다.★)
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'

# (1) 파일 읽기 
file = open(path + "/ftest.txt", mode = 'r') # 읽어올 목적으로 파일 객체를 만든다. ★★★
print(file.read()) # 파일 전체 읽기(파일 객체 사용)
file.close() # 객체 닫기 # 메모리에서 빠짐 ★★★

# 방법 2

# 경로 확인 및 이동
import os 
dir(os)
'''
getcwd() : 현재 작업 위치(경로) 확인 
chdir() : 경로 이동시킬 때 
'''
os.getcwd() # >> 'C:\\ITWILL\\2_Python\\workspace\\Python_practice1\\chap06_File'

path2 = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'
os.chdir(path2) # 해당 경로로 이동해서 해당 경로의 파일을 불러올 수 있다. 
help(os.chdir)
file2 = open('ftest.txt', mode = 'r')
print(file2.read())
file2.close()


# (2) 파일 쓰기(자동 생성) - mode = 'w'
ftest2 = open('ftest2.txt', mode = 'w') # 해당 파일이 만들어진다. (지금 작업 경로에 만들어짐) 
# 단 기존에 있으면 덮어씌운다. 
ftest2.write('my first text~~~') # 생성한 파일에 내용 쓰기 
ftest2.close()

# (3) 파일 쓰기(자동생성) 단, 내용추가로 - mode = 'a'
 # 근데 기존에 없으면 파일 생성됨
path3 = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File'
ftest3 = open(path3 + '/ftest2.txt', mode = 'a') # 해당 파일에 접근해서 추가할 것이다. 
# 단 기존에 있으면 덮어씌운다. 
ftest3.write('\n my second text~~~') # 생성한 파일에 내용 쓰기 
ftest3.close()

ftest3 = open(path3 + '/ftest2.txt', mode = 'r')
print(ftest3.read())


# (4) 다양한 파일 읽기 - read() 메소드에서 파생 
'''
file.read() # 전체 내용 읽기 ,string
file.readline() #전체 내용 중 한 줄 읽기 ,string
file.readlines() # 전체 내용 줄 단위로 읽는다. (한 줄 단위로 list화)
'''
file = open(path + "/ftest.txt", mode = 'r') # 1) 파일 객체 만들기
# 2) 파일 객체 사용
dir(file) #file이라는 객체에 사용할 수 있는 메소드를 알려준다. 

data = file.read() # read()는 통 문자열로 읽어옴  
print(data)
print(type(data)) # class 'string' 

line = file.readline() 
print(line) # 안나옴 # 위에서 이미 읽었기 때문에 ★★★
# 그래서 close()로 객체를 닫아주고 다시 열어야 함...
file.close()
file = open(path + "/ftest.txt", mode = 'r') 
line = file.readline() # 첫 줄
print(line)
line = file.readline() # 두번째 줄
print(line)

# readlines() 
lines = file.readlines() 
print(lines) 
print(type(lines)) # >> class 'list'


#
words = [] # 단어 저장하기

# 디렉토리 어딘지 확인하기 
os.getcwd(file) # >> 이렇게 쓰는 거 아님. 인자 안씀 ★★★
help(os.getcwd)
current_directory = os.getcwd() # 경로에 대한 객체를 생성하는 형태로 쓴다. 
print(current_directory)


for i in lines : 
    for j in i.split(): # 디폴트는 공백과 줄바꿈 둘다 대상임 ★★★
        words.append(j)

print(words)
print(len(words)) # 22 개의 원소



words2= []
# path 이용
print(path)
file = open(path + '/ftest.txt', mode = 'r') # 파일 객체 생성 

while True : # 파일 내 몇 줄인지 모르니까 
    line = file.readline() # 한줄씩 계속 읽다가  
    if line : # 읽히면 
        # print(line) # 문장 끝 불용어(\n) 까지 포함되어서 출력됨
        line = line.strip() # 문장 끝 불용어 제거 ★★★ 또는 rstrip() 사용하자 
        # for i in line :  # [틀림] 이렇게 하면 line 이라는 string 이 전부 쪼개짐
        for i in line.split(' '):
            words2.append(i)
    else :  # 안읽히면
        break # 끝난 거니까 탈출문
    
print(words2)
help(line.strip)
