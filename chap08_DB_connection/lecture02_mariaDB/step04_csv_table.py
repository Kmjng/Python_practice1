# -*- coding: utf-8 -*-
"""
step04_csv_table.py

exam04에서 작성한 student 테이블에 레코드 추가하기  
 - student.csv 파일 내용으로 레코드 삽입과 조회  
"""

import pandas as pd # csv file 읽기
import pymysql # driver 

path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap08_DB_connection/data'

student = pd.read_csv(path + '/student.csv')
student.info()

print(student)
'''
    sno name           tel  deptno  propno
0  9511  김신영  055)333-6328     101    1002
1  9512  신은경  051)418-9627     102    2002
2  9513  오나라  051)724-9618     202    4003
3  9514  구유미  055)296-3784     301    4007
4  9515  임세현   02)312-9838     201    4001
5  9612  김진욱  055)488-2998     102    2001
6  9613  안광훈  053)736-4981     201    4002
7  9614  김문호  02)6175-3945     201    4003
8  9615  노정호  051)785-6984     301    4007
9  9714  김주현  055)423-9870     102    1001

'''
# 1. 각 칼럼 추출  # DB.칼럼명 ★
sno = student.sno
name = student.name
tel = student.tel
deptno = student.deptno
propno = student.propno

student.shape # >> (10,5)
len(student)

type(student) # >> pandas.core.frame.DataFrame (2차원)
type(sno) # >> pandas.core.series.Series (1차원)  (n,)
sno.shape # >> (10,)

# 판다스는 DataFrame과 Series 두가지 자료구조를 제공한다. 
# 넘파이처럼 n차원까지 제공 못함

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
    cursor.execute("show tables") # table 목록 조회 
    tables = cursor.fetchall() # table 목록 가져오기 
    
    sw = False # off
    for table in tables : 
        if 'student' in table :
            sw = True # on
    
    # 2. 레코드 추가 & 조회 
    if sw : # table 있는 경우   
        print('레코드 추가') # 레코드 추가  
        size = len(student)
        
        for i in range(size) : 
            sql = f""" insert into student values
            ({sno[i]},'{name[i]}','{tel[i]}',{deptno[i]},{propno[i]}) """ # series 객체
            cursor.execute(sql)
        conn.commit() 
        
        cursor.execute('select * from student')
        rows = cursor.fetchall() 
        
        for row in rows: 
            print(row)
        
        print('전체 레코드수: ',len(rows))
    else : # table 없는 경우         
        print('student 테이블이 없습니다.')        
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close()
    conn.close()
    
    
    
    
    