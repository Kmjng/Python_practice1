# pip install openpyxl 판다스에서 엑셀파일 처리 하는 모듈


import pandas as pd

# 파일 경로
path = r"C:\Users\user\Desktop\IT"

# 파일을 읽어들입니다.
file = open(path+'\crawling.txt', mode='r', encoding='utf-8') # 파일 객체
lines = file.readlines()  # 파일 내용을 리스트로 읽어옵니다.
file.close()  # 파일을 닫습니다.

# 데이터프레임 생성
data = pd.DataFrame({'Data': lines})

# 데이터를 엑셀 파일로 저장합니다.
excel_file = "crawling.xlsx"
data.to_excel(excel_file, index=False)  # index를 포함하지 않고 데이터를 저장합니다.
