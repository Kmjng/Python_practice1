'''
step03 관련 문제

문2) 여러 줄의 문자열(multiline)에서 공백을 기준으로 단어(token)을 추출하고, 단어 개수를 출력하시오.
   
   <출력 결과>    
   안녕
   Python
   세계로
   오신걸
   환영
   합니다.
   파이션은
   비단뱀
   처럼
   매력적인
   언어
   입니다.
   
   단어 개수 : 12
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""

# 방법 1
words=[]

for i in multiline.split(sep='\n'):
    for j in i.split(sep=' '):
        words.append(j)
        print(j)
print('단어 개수: ',len(words))

# 방법 2
words=[]

for i in multiline.split(): # \n과 공백 모두 포함 split
    words.append(i)
    print(i)
print('단어 개수: ',len(words))