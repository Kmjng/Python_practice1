# -*- coding: utf-8 -*-
"""
문5) 아래 코드는 labels.json 파일의 자료를 읽어와서 labels의 리스트에 저장된 상태이다. 
    이때 labels의 리스트 객체를 pickle 파일로 저장한 후 읽어와서 파일의 내용을 출력하시오.
    조건> path 경로에 'labels.pickle' 파일명으로 저장

json에서 피클로 바꾸려면 디코딩해서 파이썬 딕셔너리 작업후 변경해줘야 하는 듯 
"""

import json


path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'


# json file 읽기 
file = open(path + "/labels.json", mode='r', encoding='utf-8')

labels = json.load(file)  # 대괄호 형태의 json 파일 디코딩
        
print(labels)   
type(labels)
    
import pickle 

# [단계1] pickle file save
file_pick = open(path + '/labels.pickle', mode = 'wb') #'wb' => binary 형태로 인코딩한다. 
# save할 때 이 과정 빼먹음 주의 !!!!
pickle.dump(labels, file_pick) 
file_pick.close() 

# [단계2] pickle file load
file2 = open(path + '/labels.pickle', mode = 'rb') # 'rb' => binary 형태를 디코딩한다. 
file2.read() # >> 이렇게 말고! 
file2.load() # >> AttributeError: '_io.BufferedReader' object has no attribute 'load'
p = pickle.load(file2) 
print(p) # binary로 저장되어 있는 pickle을  위 방법으로 디코딩해서 읽었다. 
