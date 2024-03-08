'''
우편번호 찾기 - 52,144개
[우편번호]tab[도/시]tab[구]tab[동]tab[세부주소] 
[135-807]  서울  강남구  개포1동 우성3차아파트  (1∼6동)
[135-807]  서울  강남구  개포1동 우성3차아파트 [세부주소 없음]
'''

# 파일 경로 
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'


# ★★★ startswith() 함수를 사용해 우편번호 파일 읽기 

# 파일 상태 확인 
# 파일 보면 띄어쓰기와 탭으로 구분되어 있음. 
file = open(path + '/zipcode.txt', mode = 'r', encoding='utf-8') #enconding 한글문서 저장방식(utf-8, euc-kr)
line = file.readline() # 첫줄 읽기  (string 임)
print(line)		  
# >> ﻿135-806	서울	강남구	개포1동 경남아파트		1

tokens = line.split(sep='\t') # 탭키를 의미하는 escape 
tokens #>> ['\ufeff135-806', '서울', '강남구', '개포1동 경남아파트', '', '1\n']
tokens[3] # >> '개포1동 경남아파트'
# \ufeff 는 뭐지 ?????


dong = input('무슨 동: ')
cnt =0
while True : 
    
    if line :
        tokens = line.split(sep='\t')
        if tokens[3].startswith(dong) : # startswith() ★★★ 해당 접두어와 동일하면 True 
            print(tokens[0], tokens[1], tokens[2], tokens[3])
            cnt += 1
        line = file.readline() # 한줄 읽어라 - while로 반복, line이 남아있을 때 까지 
        
    else :
        break 
print('검색된 주소의 수: ',cnt)

file.close() # 중요★★ 한번 다 돌고나면 읽기 끝나니까 


