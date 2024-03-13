# -*- coding: utf-8 -*-
"""
step02_CRUD.py
Create - insert
Read 
Update
Delete 
"""

import oracledb

try :
    # db 연동 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger') 
    # sql문 실행 객체 
    cursor = conn.cursor()    
    
    
    # 2. 레코드 삽입 : Create(insert) - 50번부서 추가
    '''
    code = int(input('code input: '))
    dname = input('dname input: ')
    loc = input('location input: ')
    query = f"""insert into dept01 
    values({code},'{dname}','{loc}')
    """ # 반드시 입력받는 string에 해당하는 녀석들은 ''따옴표 해주기 ★★★
    cursor.execute(query)
    conn.commit() #insert하고 꼭 커밋해줘야 함
    '''
    
    # 3. 레코드 수정 : Update
    '''
    deptno = int(input('deptno Update input: ')) # 50
    dname = input('dname Update input: ')   # 기획실 -> 영업부
    loc = input('location Update input: ') # 서울시 -> SEOUL 
    query = f"""update dept01 set dname ='{dname}',
    loc='{loc}' where deptno = {deptno}
    """
    cursor.execute(query) #실제 레코드 수정
    conn.commit() # db반영
    '''
    
    # 4. 레코드 삭제 : Delete  (if문과 응용가능)
    code = int(input('code delete input: '))
    

    query1 = f"""SELECT * FROM dept01 WHERE deptno ={code}
    """
    cursor.execute(query1) #레코드 조회 실행 
    row = cursor.fetchone() # 레코드 하나 가져오기 ★★★
    if row : # ★★★
        query2 = f"""DELETE FROM dept01 WHERE deptno ={code}
        """
        cursor.execute(query2)
        conn.commit() 
    else : 
        print("해당부서번호가 없습니다.")
    
    
    
    # 1. 레코드 조회 : Read(select) 
    query = "select * from dept01" # 부서테이블 확인 
    cursor.execute(query)    
    dataset = cursor.fetchall() # 전체 레코드 
    print('-'*40)
    print('code\t name\t\t\t  loc') 
    print('-'*40)
    for row in dataset :
        print("{0:^4}\t{1:<12}\t{2:<5}".format(row[0],row[1],row[2]))
        # {색인: 정렬방식 자릿수}
        # {}안에 들어가는 ^, <, > 는 정렬(가운데정렬 따위), 뒤에는 자릿수 
        
    print('-'*40)
    print('전체 레코드 수 : ', len(dataset))        
    
    
    
    
except Exception as e :
    print('db error :', e)  
    conn.rollback() # DML 명령어 취소      
finally :
    cursor.close()
    conn.close()

# 이렇게하면 매번 주석처리하기 귀찮으니
# 메뉴를 만들면 좋을 것 
# while 문으로 메뉴를 만든다. 