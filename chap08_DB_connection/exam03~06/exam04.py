# -*- coding: utf-8 -*-
"""
문제4) HidiSQL을 이용하여 다음과 같은 단계로 student 테이블을 만들고, 
      DB 연동 프로그램으로 레코드를 추가하고, 조회하시오.
  
단계1> HidiSQL 이용 : student 테이블 만들기(maria_student.sql 파일 참고) 
create or replace table student( 
  sno int primary key,              
  sname varchar(10) not null,                        
  tel varchar(15),     
  deptno int,                
  profno  int                
);  


단계2> DB 연동 프로그램 작성 : 테이블에 레코드가 없으면 레코드 추가(아래 3개)  
insert into student values (9411,'서진수','055)381-2158',201,1001);
insert into student values (9413,'이미경','02)266-8947',103,3002);
insert into student values (9415,'박동호','031)740-6388',202,4003);

단계3> DB 연동 프로그램 작성 : 테이블에 레코드가 있으면 레코드 조회(select)   
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
    
    # 1. table 유무 판단 : student 
    cursor.execute('show tables')
    tables = cursor.fetchall()
    print(tables,'\n---------')
    
    match = False 
    for table in tables: 
        if "student" in table: 
            match = True
            
        else: 
            pass
    # 2. 레코드 추가 or 레코드 조회 
    if match : # True 이면 
        query = """select * from student """
        cursor.execute(query)
        select = cursor.fetchall() 
        
        for row in select:
            if not(row):
                query1 = """insert into student values (9419,'서진수','055)381-2158',201,1001);"""
                query2 = """insert into student values (9413,'이미경','02)266-8947',103,3002);"""
                query3 = """insert into student values (9415,'박동호','031)740-6388',202,4003);"""
                
                cursor.execute(query1)
                cursor.execute(query2)
                cursor.execute(query3)
        print('레코드 조회:\n',select)     
    else : 
        print('student 테이블 없음~')
        query = """
        CREATE or REPLACE TABLE student( 
          studno int primary key,              
          sname varchar(10) not null,                        
          tel varchar(15),     
          deptno int,                
          profno  int                
        ); 
        """
        cursor.execute(query)
        conn.commit()
        
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
'''
레코드 추가 (insert) 에 대해서 


insert_queries = [
    "insert into student values (9411,'서진수','055)381-2158',201,1001)",
    "insert into student values (9413,'이미경','02)266-8947',103,3002)",
    "insert into student values (9415,'박동호','031)740-6388',202,4003)"
]

for query in insert_queries:
    cursor.execute(query)

insert_queries = """
insert into student values (9411,'서진수','055)381-2158',201,1001);
insert into student values (9413,'이미경','02)266-8947',103,3002);
insert into student values (9415,'박동호','031)740-6388',202,4003);
"""
cursor.execute(insert_queries)


'''
    