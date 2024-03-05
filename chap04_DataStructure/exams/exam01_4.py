# -*- coding: utf-8 -*-
"""
문4) 다음 origin_data의 각 리스트에 포함된 두 개의 단어를 하나로 묶어서
    pro_data 리스트에 추가한 후 각 원소를 줄단위로 출력하시오.
    
    힌트 : join() 함수 이용
    
    예) ['양말', '신발'] -> ['양발 신발']
           
    
 <출력결과> 
양말 신발
강아지 고양이
대한민국 수도 서울
"""

origin_data = [['양말', '신발'], ['강아지', '고양이'], ['대한민국', '수도', '서울']]
pro_data = [] # 처리 결과 저장

for i in origin_data : 
    pro_data.append(' '.join(i))  # i 가 리스트로 원소들이 분리되어 있어서 join() 가능 
    print(' '.join(i))

print(pro_data)


# 방법 2. 리스트 컴프리핸션 
pro_data2 = [' '.join(i) for i in origin_data]
print(pro_data2)

