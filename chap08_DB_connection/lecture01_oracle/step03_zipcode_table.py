# -*- coding: utf-8 -*-
"""
step03_zipcode_table.py

레코드가 없는 테이블에 값 입력하기

<< 작업순서 >>
1. table 생성 : sql developer에서 작업 (oracle_zipcode.sql 참고)   
2. zipcode.txt -> 서울 지역 -> 레코드 추가    
3. 레코드 조회(동 or 구 검색)

** oracle_zipcode.sql 내용 **
-- 우편번호 저장 테이블 (서울지역 한정)
create table zipcode_tab(
zipcode char(14) not null,  -- 우편번호
city varchar(15) not null,  -- 시
gu varchar(20) not null,   -- 구
dong varchar(150) not null,-- 동
detail varchar(50)      -- 상세주소(null 허용)
);


"""

import oracledb

path=r'C:/ITWILL/2_Python/workspace/Python_practice1/chap08_DB_connection/data'
path2=r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    
    # sql문 실행 객체 
    cursor = conn.cursor() 
    
    # 1. 레코드 조회 
    cursor.execute("select * from zipcode_tab")
    datasest = cursor.fetchall() # 검색 레코드 가져오기 
    
    # 2. 레코드 추가(if문★★) or 조회(else문에★★)	
    if not(datasest) : # dataset이 없으면(False이면)
        print('1) 레코드 추가하겠습니다.')
        
        file = open(path2+'/zipcode.txt',mode = 'r', encoding='utf-8') # 주소정보들어있는 txt파일
        line = file.readline() # list 타입
        # 135-807	서울	강남구	개포1동 현대1차아파트	(101∼106동)	9
        while line : # 내용이 있으면 반복
            token = line.split(sep='\t') 
            if token[1] =='서울' : # 잘 보면 '서울 강남구' 가 tab으로 나눠져 있음~
                zipcode = str(token[0]) # '135-807' ##★★★★숫자랑 뺄셈으로 인식해서 str() 해줘야 함
                city = token[1] ; gu = token[2]
                dong = token[3] ; detail = token[4]
                
                if detail :  # 다섯번째 칼럼에 값이 없을 경우
                    query = f'''INSERT INTO zipcode_tab VALUES('{zipcode}','{city}','{gu}','{dong}','{detail}')
                    '''
                else :
                    query = f'''INSERT INTO zipcode_tab(zipcode, city, gu, dong) VALUES('{zipcode}','{city}','{gu}','{dong}')
                    '''
                cursor.execute(query) # ★★★
                conn.commit() 
            line = file.readline() # 2번째 줄열리고 while문 처음으로 돌아감 
            # 처음에 while line으로 시작했으므로, while문 처음에 readline()이 올 수 없음.. 
                
                
        # while문 끝내고         
        file.close()
        print('레코드 삽입 성공~')
    else : 
        print('2) 레코드 조회') 
        choice = int(input('1. 동, 2. 구 :'))
        if choice == 1: 
            dong = input('검색할 동 입력: ') # %개포%
            query = f"select * from zipcode_tab where dong LIKE '%{dong}%' " # [SQL] like "~"안된다 
            cursor.execute(query)
            dataset = cursor.fetchall() # 조회된 모든 레코드 가져오는 메소드 => 리스트형
            for row in dataset: 
                print(row) #tuple 
                print('조회된 레코드 수 : ', len(dataset))
        elif choice ==2 :
            gu = input('검색할 구 입력: ')
            query = f'select * from zipcode_tab where dong LIKE "%{gu}%" '
            cursor.execute(query)
            dataset = cursor.fetchall()
            for row in dataset: 
                print(row) #tuple 
                print('조회된 레코드 수 : ', len(dataset))
        else: 
            print("잘못입력했습니다.")
except Exception as e :
    print('db error : ', e)
    conn.rollback() 
finally :
    cursor.close()
    conn.close()
    
    
    
    
    
    
    