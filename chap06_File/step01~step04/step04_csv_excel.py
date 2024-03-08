'''
csv, excel file read
 - 칼럼 단위로 작성된 excel 파일 유형 읽기
'''
# 판다스 설치 및 확인

import pandas as pd

# ★★★ pandas 없으면 설치하기 ★★★

# Anaconda prompt 앱에서 
# pip install pandas 를 입력한다.

dir(pd)
'''
read_csv(file)
read_excel(file)
read_html(file)
read_json(file)  
read_pickle(file)
# 인수 전부 파일명 

'''

##########################
### 1. csv file     판다스와 함께 한다.
##########################

'''
앞에서는 txt 파일 사용했음  
read() 

'''


# 1) file 읽기 및 내용 보기  
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data' 
bmi = pd.read_csv(path + '/bmi.csv', encoding='utf-8')
# 판다스 라이브러리로 만든 객체!
dir(bmi) # bmi 객체에서 사용할 수 있는 메소드 확인 

# 판다스 라이브러리의 매소드들
print(bmi.info()) # info() 메소드 : 객체에 대한 정보 
help(bmi.info()) # >> <class 'pandas.core.frame.DataFrame'>

''' >> 
<class 'pandas.core.frame.DataFrame'> # 행렬 구조(table)
RangeIndex: 20000 entries, 0 to 19999 # 행의 길이
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   height  20000 non-null  int64 
 1   weight  20000 non-null  int64 
 2   label   20000 non-null  object
dtypes: int64(2), object(1)
memory usage: 468.9+ KB
None
'''



print(bmi.head()) # 안에 인수 넣으면 필요한 행 만큼 확인할 수 있음 
print(bmi.tail())
    



# 2) 칼럼 단위 호출(추출) 해야 데이터 처리할 수 있다. 
height = bmi.height
weight = bmi.weight
label = bmi.label


# 3) 칼럼 단위 연산 
# 내장 함수    
print('max height:', max(height))
print('max weight:', max(weight))

print('height mean : ', sum(height) / len(height))
print('weight mean : ', sum(weight) / len(weight))    

    
# pandas 내의 함수 
# mean() 메소드
height.mean() 


# label 빈도수 
# value_counts() 메소드
label_count = label.value_counts()
print(label_count)



# 4) 행열 참조 
# loc[행범위, 열범위] / iloc[행범위, 열범위]
# [1] loc 속성 : ★★★ 명칭 기반 ★★★

# 일단 테이블 확인해봅시다. 
bmi.shape # (20000,3) 20000개의 행, 3개의 열

bmi.loc[0] # bmi.loc[0, :] : 1행 전체(열 쪽 콜론은 생략 가능하다.) 
bmi.loc[:4] # 5행 전체★★★ : 숫자를 명칭으로 해석해서 0행부터 4행까지 조회한다. 

bmi.loc[:,'height':'label'] # 연속 칼럼 
bmi.loc[:,['height','label']] # 비연속 칼럼 몇가지를 사용할 경우

# [2] iloc 속성 : ★★★ 위치(숫자) 기반 ★★★ integer location 
bmi.iloc[0] # bmi.loc[0]과 똑같다. 
bmi.iloc[:4] # 4행★★★  # 색인으로 인식한다. 0,1,2,3행

bmi.iloc[:, 0:3] # 연속 칼럼 
bmi.iloc[:, [0, 2]] # 비연속 칼럼 

# ★★★★★★★★★★
bmi.iloc[100:200, [0,2]] # 100~ 199 행, 첫번째 열과 세번째 열
bmi.loc[100:199,['height','label']]

# 5) 조건 검색 : 조건으로 행 선택(비교, 논리연산자 사용) 
bmi[(bmi.height >= 180)] # 비교연산자 
bmi[(bmi.weight >= 50) & (bmi.weight <= 70)] # 논리연산자 and 
bmi[(bmi.label=='thin') | (bmi.label=='fat')] # 논리연산 or
bmi[~(bmi.label=='normal')] # 논리연산 not


##########################
### 2. excel file 
##########################

# 1) file 읽기 및 내용보기 
# pd.ExcelFile() 
# .parse() 
ex = pd.ExcelFile(path + '/sam_kospi.xlsx')
kospi = ex.parse('sam_kospi') # 엑셀 파일은 파싱을 꼭 해줘야 함
print(kospi)

# 칼럼 정보 
print(kospi.info())

# 2) 컬럼 추출 
high = kospi.High
low = kospi.Low

# 3) 칼럼 단위 통계  
print('High mean :', high.mean())
print('Low mean :', low.mean())




