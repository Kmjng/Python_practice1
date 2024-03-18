'''
패키지(Package) = 폴더 
 - 유사한 모듈(python file)을 꾸러미로 묶어놓은 단위

모듈(Module) = 파일 
 - 함수와 클래스로 구성된 python file(*.py)
'''

# 주의 : 임포트할 패키지의 상위 경로 변경 

import os # os 관련 함수 : file 경로 확인, 변경
#os.getcwd() # 경로 확인 

os.chdir(r'C:/ITWILL/2_Python/workspace/Python_practice1/chap07_txt_pre')# 디렉터리 변경 


# 형식) from 패키지명.모듈명 import 함수명 
from step03_04.step03_text_preprocessing import clean_text # 함수 or 클래스


texts = ['afase$$$ $%# asdf','nakfnjr akj;;;  sl']
clean_text(texts)





