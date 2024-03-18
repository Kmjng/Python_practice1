# -*- coding: utf-8 -*-
"""
텍스트 전처리 : 특수문자, 불용어 처리 
"""

import re # re 모듈 가져오기 

# 전처리 텍스트  
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,  A124&***$?']

print([re.findall('\w+',i) for i in texts])


# 텍스트 전처리 함수 정의 
def clean_text(texts) : # list input

    # 단계1 : 소문자 변경
    texts_re = [st.lower() for st in texts] # list -> string 추출 


    # 단계2 : 문장부호 & 특수문자 제거     
    texts_re2 = [re.sub(r'[^\w\d\s]', '', st) for st in texts_re]
    # re.sub()로 메타문자들로 \w,\d,\s 아닌것들 => 문장부호, 특수문자 지정
    

    #단계3 : 숫자 제거 : 변수 = [실행문(method/func) for 변수 in 열거형객체]
    texts_re3 = [re.sub('[0-9]', '', st) for st in texts_re2]    
   
    
    # 단계4 : 공백(white space) 제거
    texts_re4 = [re.sub(r'\s+', ' ', st) for st in texts_re3]
    # \s+ 공백 제거(1칸 이상 공백 -> 전부 1칸 공백) 

    return texts_re4

result_texts = clean_text(texts)
print('정제전: ',texts,'\n정제후 :',result_texts)

clean_text('AFAB54747,asabag?') # 이렇게하면 string을 분해해서 for문 돌림 ★★★★
# 위에서 작성한 clean_text()함수는 인자에 리스트형을 넣어야 용도에 맞게 사용가능하다. 



