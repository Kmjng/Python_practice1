# -*- coding: utf-8 -*-
"""
step01_OracleDB_test.py
"""


import oracledb #driver -> 프로그램(python)과 db(오라클)을 연결해주는 드라이버 
dir(oracledb)
'''
★★ connect() : db 연결하는 함수
version() : 버전 확인 
'''
oracledb.version  # >> 2.1.0

# dir(conn) >>  cursor(), commit(), rollback()   
'''
★★ cursor(): cursor객체 생성.  
커서 객체는 하나의 DB connection에 대하여 독립적으로 SQL 문을 실행할 수 있는 작업환경을 제공하는 객체

execute(쿼리객체) : 쿼리문 실행하는 메소드

fetchall() : 조회된 모든 레코드 가져오는 메소드 => 리스트형으로 저장
fetchone() : 레코드 하나 
'''  

try :
    # 1. db 연동시키는 connection 객체 생성 ★★
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE', #dsn: IP주소:포트번호(오라클포트번호1521임)/DB이름
                                                # Data Source Name (고정IP 혹은 유동 IP..)
                            user='c##scott',
                            password='tiger')
    
    # 2. sql문 실행 객체 
    cursor = conn.cursor() #cursor 객체를 connect 객체에서 만듦
    
    # 3. sql문 작성 & 실행 
    query = "select * from emp" #파이썬에선 단순 문자열에 불과
    cursor.execute(query) # 이 문자열을 db로 실행시킬 수 있다. 
    
    # 4. 레코드 가져오기 & 출력     
    dataset = cursor.fetchall()
        
    for row in dataset :
        print(row) # tuple형으로 보여줌
        print(row[0],row[1],row[5]) #인덱스 붙여서 원하는 칼럼 선택 가능
    print('전체 레코드 수 :',len(dataset))
except Exception as e : #예를들어 잘못된 쿼리문으로 객체를 만들었따던가..
    print('db error : ', e)
finally :
    # 객체 닫기 # 객체를 닫을 때에는 역순으로 닫는다. ★★★★★★
    cursor.close()
    conn.close()















