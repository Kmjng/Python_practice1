'''
문5) 다음 texts의 텍스트를 대상으로 단계별로 텍스트를 전처리하는 함수를 완성하고, 전처리 전 텍스트를 인수로 
    함수를 호출하여 텍스트 전처리 결과를 확인하시오.(아래 출력 예시는 전처리 전과 후 비교) 

<텍스트 전처리 전> 
[' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

<텍스트 전처리 후> 
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''


import re #.re.sub


# 전처리 전 텍스트
texts = [' 우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


print('<텍스트 전처리 전>')
print(texts)

def clean_text(texts) :  

    # 1. 소문자 변경 
    texts2 = [i.lower() for i in texts]
    # 2. 숫자 제거 
    texts3 = [re.sub('\d','',i) for i in texts2]    # 또는 '[0-9]'
    # 3. 문장부호 & 특수문자 제거 
    texts4 = [re.sub('[^\w\s]','',i) for i in texts3]
    # 4. 영문자 제거 
    texts5 = [re.sub('[a-z]','',i) for i in texts4]
    # 5. 공백 제거(1칸 이상 공백 -> 전부 1칸 공백)
    texts6 = [re.sub('\s+',' ',i) for i in texts5]
    return texts6

result = clean_text(texts)
print(result)
