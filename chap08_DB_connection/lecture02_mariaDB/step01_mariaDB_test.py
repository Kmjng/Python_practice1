# -*- coding: utf-8 -*-
"""
step01_mariaDB_test.py
"""

import pymysql # driver 

dir(pymysql)
'''
connect() : db 연동 
version_info() 

'''
#(1)
def connect(user,pwd): #기존에 connect()가 있는데 똑같은이름으로 만들어도되나????????
    print(user)
    print(pwd)

dir(pymysql.connect)
conf ={'user':'scott','pwd':'tiger'}

connect(conf) # [오류] 이렇게 하면 주소만 받음
connect(**conf) # 패킹연산자를 통해 주소에 가서 실인수인 key와 value를 받음

# (2) 
config = {
    'host' : '127.0.0.1',
    'user' : 'scott',
    'password' : 'tiger',
    'database' : 'work',
    'port' : 3306,
    'charset':'utf8',
    'use_unicode' : True} # 환경변수를 dict형으로 지정해서 사용함

try :
    # 1. db 연동 객체 생성 
    conn = pymysql.connect(**config) # ** 로 
    
    # 2. sql문 실행 객체 생성
    cursor = conn.cursor()
    
    # 3. sql문 실행 (조회)
    query = "select * from goods"
    cursor.execute(query)
    
    dataset = cursor.fetchall()
    

    #for row in dataset :
    #    print(row[0], row[1], row[2], row[3])   


    
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()
















