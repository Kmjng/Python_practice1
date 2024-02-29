'''
문5) 다음과 같은 2개의 파일 경로를 대상으로 각각 파일명을 추출하여 
       출력하시오.

  <출력결과>
  파일명1: emp.xlsx
  파일명2: report.docx
'''

file_path1 = "/user/itwill/emp.xlsx"

file_path2 = "/home/user/documents/report.docx"



# 방법 1 
path1 = file_path1.split('/') #split해서 리스트화
path2 = file_path2.split('/')
print('파일명1: ',path1[-1], '\n파일명2: ',path2[-1]) #리스트 마지막요소

