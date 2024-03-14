# -*- coding: utf-8 -*-
"""
step02_CRUD.py

 CRUD : Create(insert), Read(select), Update, Delete
"""

import pymysql

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
    
    
    # 3. 레코드 수정 : Update  
    '''
    code = int(input('update code input : '))
    su = int(input('update su input : '))
    dan = int(input('update dan input : '))
    
    query = f"""update goods set su={su}, dan={dan}
              where code={code}"""
    cursor.execute(query)
    conn.commit() # db 반영 
    '''

    # 2. 레코드 추가 : Create
    '''
    code = int(input('code input : '))
    name = input('name input : ')
    su = int(input('su input : '))
    dan = int(input('dan input : '))
    query = f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(query) 
    conn.commit() # db 반영 
    '''   

        
    # 1. 레코드 조회 : Read   
    query = "select * from goods"
    cursor.execute(query)    
    dataset = cursor.fetchall() # 전체 레코드 
    
    print('-'*40)
    print('code\t name\t   su\t    dan')
    print('-'*40)
    for row in dataset :
        print("{0:^4}\t{1:<5}\t{2:>5}\t{3:8,d}".format(row[0],row[1],row[2],row[3]))
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))        


    # 4. 레코드 추가 : Create
    '''
    code = int(input('code input : '))
    name = input('name input : ')
    su = int(input('su input : '))
    dan = int(input('dan input : '))
    query = f"insert into goods values({code},'{name}',{su},{dan})"
    cursor.execute(query) 
    conn.commit() # db 반영 
      '''
    # 5. 레코드 수정 : Update  
    '''
    code = int(input('update code input : '))
    su = int(input('update su input : '))
    dan = int(input('update dan input : '))
    
    query = f"""update goods set su={su}, dan={dan}
              where code={code}"""
    cursor.execute(query)
    conn.commit() # db 반영 
    '''
    
    # 6. 레코드 삭제 :Delete
    '''
    code = int(input('delete code input:'))
    cursor.execute(f'select * from goods where code = {code}')
    row = cursor.fetchone()
    
    if row : 
        cursor.execute(f'delete fromm goods where code = {code}')
        # conn.commit()
    else : 
        pass
    '''
 
except Exception as e :
    print('db error :', e)
    conn.rollback() # 이전 상태 리턴     
finally :
    cursor.close(); conn.close()

