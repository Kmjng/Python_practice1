'''
문2) ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어를 카운트 하시오. 


문단 내용 
['programming is fun', 'very fun!', 'have a good time', 'mouse is input device', 'keyboard is input device', 'computer']
문장 수 :  6

단어 내용 
['programming', 'is', 'fun', 'very', 'fun!', 'have', 'a', 'good', 'time', 'mouse', 'is', 'input', 'device', 'keyboard', 'is', 'input', 'device', 'computer']
단어 수 :  22
'''
# ★★★★★★★★★★★★★★★★★★★★★★
 
import os

# 파일 읽기 
os.chdir(r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data') #해당 경로로 이동
file = open("ftest.txt", mode = 'r') # 현재 작업 경로 변경한 곳의 파일 

texts = file.readlines() # 줄단위 읽기 (list로 토큰화됨) ★★★★

print(texts) # list 반환돼서 나타남

sentences = []
words = [] 

for i in texts : 
    i = i.strip()
    sentences.append(i) 
    # for j in sentences: 이러면 sentences 리스트가 돌아감
    for j in i.split() : 
        words.append(j)



print(f'문단 내용\n{sentences}\n문장 수 : {len(sentences)}')
print(f'단어 내용\n{words}\n단어 수 : {len(words)}')
