# -*- coding: utf-8 -*-
"""
step03_emp_table.py

1. HidiSQL에서 emp_test table 생성 후 레코드 추가(maria_emp_test.sql 참고) 

2. 테이블 유무를 판단
   -> 테이블 있으면 레코드 조회
   -> 테이블 없으면 '테이블 없음' 메시지 출력 
"""

import pymysql # driver

config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True}

try :
    # db 연동 객체 생성 
    conn = pymysql.connect(**config)
    # sql문 실행 객체 
    cursor = conn.cursor()    
    
    # 1. table 유무 판단 : emp_test 
    # 1.1. 테이블 목록 조회 
    cursor.execute("show tables") # table 목록 조회 # mysql 명령어: show tables
    tables = cursor.fetchall() # table 목록 가져오기 
    print(tables)
    '''
    (('dept_test',), ('dept_test2',), ('emp',), ('emp_test',), 
     ('goods',), ('professor',), ('student',))
    원소 하나인 튜플 
    '''
    
    
    # emp 테이블 조회 : 스위칭 (Switching) 기법 ★★★★ 
    sw = False # 초기값 : 테이블 없음 
    
    for table in tables: 
        if 'emp_test' in table: # ('dept_test',) 튜플 안에 탐색
            sw = True 

    # 2. 레코드 조회/추가 or table 생성         
    if sw : # table 있는 경우 
        print('테이블 있음 ^_^')       
        
        # 테이블 레코드 조회
        query = "select * from emp_test"
        cursor.execute(query)  
        dataset = cursor.fetchall()
        
        print('전체 레코드 수:',len(dataset))
        
    else : # table 없는 경우                 
        print('emp 테이블 없음 ㅠㅠ')    
        # 테이블 만들기 
        query = """CREATE TABLE emp_test (
        eno int auto_increment primary KEY, -- 자동번호생성기  
        ename varchar(20) not null,
        hiredate date not null,
        sal int not null,
        bonus int default 0,
        job varchar(20) not null,
        dno int);
        """        
        cursor.execute(query)
        
        
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()    
    
   
    
    
    
    
    
    
    
    



