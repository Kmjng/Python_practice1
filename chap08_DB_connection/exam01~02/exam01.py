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

# 부서번호 조회 함수 (for 효율성)
def select(code) :
    query1 = f"select * from dept03 where deptno = {code}"
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
        
        if menu == 1 :
            print("1. 레코드 조회입니다.")
            choice = int(input('1. 부서조회, 2. 전체조회: '))
            if choice ==1 : 
                code = input('조회할 deptno: ')
                row = select(code) # ★★★★ 위에서 함수 정의
                if row : 
                    print(f'부서번호: {row[0]}, 부서이름:  {row[1]}, 위치:  {row[2]}')
                else : 
                    print('해당부서가 없습니다.')
                
            elif choice == 2:    
                query ="""SELECT * FROM dept03
                """
                cursor.execute(query)
                dataset = cursor.fetchall()
                print('-'*40)
                print(dataset)
                print('-'*40)
            else: 
                print('잘못입력했습니다.')
            
        elif menu == 2:
            print("2. 레코드 추가입니다. ")
            code = int(input('추가할 deptno :'))
            dname = input('dname:')
            loc = input('location: ')
            
            query =f"""INSERT INTO dept03 VALUES({code},'{dname}','{loc}')
            """
            cursor.execute(query)
            conn.commit() 
            
        elif menu == 3:
            print("3. 레코드 수정입니다. ")
            code = int(input('수정할 deptno :'))
            dname = input('dname:')
            loc = input('location: ')
            query =f"""UPDATE dept03 SET deptno ={code}, dname='{dname}', loc='{loc}'
            """
            cursor.execute(query)
            conn.commit() 
            
        elif menu == 4:
            print("3. 레코드 삭제입니다. ")
            code = int(input('삭제할 deptno :'))
            row = cursor.fetchone() # 레코드 하나 가져오기 ★★★★★★★★★★★★★★★
            if row : # row가 있으면
                query =f"""DELETE FROM dept03 WHERE deptno ={code}
                """
                cursor.execute(query)
                #conn.commit() 
            else : 
                print('해당하는 부서번호가 없습니다. ')
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
