# -*- coding: utf-8 -*-
"""
step05_join_subquery.py

1. HidiSQL SQL 파일 불러오기 & 테이블 생성 실습
  ->  maria_dept_test.sql 파일 선택 > dept_test 테이블 생성 
  ->  maria_emp_test.sql 파일 선택 > emp_test 테이블 생성 
  
2. join & subquery : emp_test vs dept_test 
  -> ANSI 표준 JOIN 
  -> subquery : 부서정보 -> 사원정보 조회 
"""

import pymysql # driver = python + DB(Mysql)

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
    
    # 1. ANSI inner join  : emp(10,20) vs dept(10,20,30)
    sql1 = """SELECT e.eno, e.ename, e.sal, d.dno ,dname, loc
    FROM emp_test e INNER JOIN dept_test d
    ON e.dno = d.dno  and e.sal >= 250""" 
    # 2. ANSI right outer join  : emp(10,20) vs dept(10,20,30)
    sql2 = """SELECT e.eno, e.ename, e.sal, d.dno ,dname, loc
    FROM emp_test e RIGHT OUTER JOIN dept_test d
    ON e.dno = d.dno  """ 
    
    cursor.execute(sql2)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    for row in dataset :
        print(row[0], row[1], row[2], row[3],row[4],row[5])   
    
    # 2. subquery 
    dno = int(input("조회할 부서번호:"))
    sql3 = f""" select * from emp where dno = (select dno from dept_test
            where dno = {dno} ) """
    cursor.execute(sql3)
    dataset= cursor.fetchall() 
    for row in dataset:
        print(row[0],row[1],row[2],row[3])
        
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
    
    
    
    
    
    
    
    