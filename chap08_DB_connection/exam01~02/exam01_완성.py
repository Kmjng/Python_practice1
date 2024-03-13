'''
문제1) 다음과 같은 메뉴를 이용하여 dept01 테이블을 관리하시오.
    [레코드 처리 메뉴 ]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력 : 
'''    

import oracledb

# 부서번호 조회 함수 
def select(code) :
    query1 = f"select * from dept01 where deptno = {code}"
    cursor.execute(query1) # 레코드 조회 
    row = cursor.fetchone() # 레코드 1개 가져오기
    return row 

try:
    # db 연결 객체 생성 
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE',
                            user='c##scott',
                            password='tiger')
    # SQL 실행 객체 생성 
    cursor = conn.cursor()    
    
    while True :  # 무한루프 
        print('\t[레코드 처리 메뉴 ]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')    
        menu = int(input('\t메뉴번호 입력 : '))
        
        if menu == 1 : # 1. 레코드 조회
            choic = int(input('1. 부서조회, 2. 전체조회 : '))
            if choic == 1 :
                code = int(input('부서번호 입력 : '))
                row = select(code) # 함수호출
                if row :
                    print(f'부서번호 : {row[0]}, 부서이름 : {row[1]}, 위치 : {row[2]}')
                else :
                    print('해당 부서가 없습니다.')
            elif choic == 2 :
                query = "select * from dept01" # 부서테이블 확인 
                cursor.execute(query)    
                dataset = cursor.fetchall() # 전체 레코드 
                
                print('-'*40)
                print('code\t name\t\t\t  loc')
                print('-'*40)
                for row in dataset :
                    print("{0:^4}\t{1:<12}\t{2:<5}".format(row[0],row[1],row[2]))
                '''
                {색인:정렬방식 자릿수} 
                정렬방식 : ^(가운데정렬), <(왼쪽 정렬), >(오른쪽 정렬)
                '''    
                print('-'*40)
                print('전체 레코드 수 : ', len(dataset))
            else :
                print('잘못 입력했습니다.')
            
        elif menu == 2: # 2. 레코드 추가
            code = int(input('code input : ')) # 50
            dname = input('dname input : ') # 기획실
            loc = input('loc input : ') # 서울시 
            
            query = f"""insert into dept01
                        values({code}, '{dname}', '{loc}')"""
            cursor.execute(query) # 실제 레코드 삽입 
            conn.commit() # db 반영 
            
        elif menu == 3: # 3. 레코드 수정 
            code = int(input('deptno update input : ')) # 50
            dname = input('dname update input : ') # 영업부
            loc = input('loc update input : ') # SEOUL
            
            row = select(code) # 부서번호 조회 함수
            
            if row :
                query = f"""update dept01 set dname='{dname}', loc='{loc}' 
                        where deptno = {code}"""
                cursor.execute(query) # 실제 레코드 수정 
                conn.commit() # db 반영
            else :
                print('해당 부서번호가 없습니다.')
                
        elif menu == 4: # 4. 레코드 삭제 
            code = int(input('deptno delete input : ')) # 50
            
            row = select(code) # 부서번호 조회 함수 
            
            if row :
                # 레코드 삭제     
                query2 = f"delete from dept01 where deptno = {code}"
                cursor.execute(query2) # 실제 레코드 삭제
                conn.commit() # db 반영
            else :
                print('해당 부서번호가 없습니다.') 
        elif menu == 5 :
            print('프로그램 종료')
            break # 반복 exit
        else :
            print('해당 메뉴는 없습니다.')
        
# DB 연결 예외 처리          
except Exception as e :
    print('db 연동 오류 : ', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close() 
