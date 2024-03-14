# -*- coding: utf-8 -*-
"""
step04_join.py
"""

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    # sql문 실행 객체 
    cursor = conn.cursor()
    
    # join  
    '''
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e, dept d
    WHERE e.deptno = d.deptno AND e.job='MANAGER'"""
    '''
    
    # ANSI INNER JOIN 
    '''
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e INNER JOIN dept d
    ON e.deptno = d.deptno AND e.job='MANAGER'  """
    '''
    # ANSI LEFT OUTER JOIN 
    sql = """SELECT e.empno, e.ename, e.sal, e.job, d.deptno
    FROM emp e LEFT OUTER JOIN dept d
    ON e.deptno = d.deptno AND e.job='MANAGER'  """
    
    cursor.execute(sql)
    dataset = cursor.fetchall()
    
    # 레코드 조회 
    for row in dataset :
        print(row[0], row[1], row[2], row[3], row[4])   
    
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
    
    
    
'''
[실습] 칼럼: 학생명, 학과, 교수번호, 교수명 
학생(student01) vs 교수(professor01) 내부조인, 외부조인 
'''


    
    