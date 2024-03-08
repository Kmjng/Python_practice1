'''
문2) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''

 
import os

# 파일 읽기 
os.chdir(r'C:\ITWILL\2_Python\workspace\chap06_FileIO\data')
file = open("ftest.txt", mode = 'r') # file 객체 생성 

texts = file.readlines() # 줄단위 읽기 

print(texts) # list 반환 

sents = [] # 문장 저장 
words = [] # 단어 저장 

for line in texts :
    sents.append(line.strip()) # 불용어(\n) 제거 
    for word in line.split() : # 공백 또는 '\n' 기준 토큰 생성 
        words.append(word)

print('문장 내용')
print(sents)
print('문장 길이 : ', len(sents))

print('단어 내용')
print(words)
print('단어 길이 : ', len(words))



