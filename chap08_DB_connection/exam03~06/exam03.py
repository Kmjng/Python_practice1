'''
문제3) goods 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
 <조건1> 전자레인지 수량, 단가 수정 
 <조건2> HDTV 수량 수정 

    [ goods 테이블 현황 ]
1 냉장고 2 850000
2 세탁기 3 550000
3 HDTV 4 1500000  <- 수량 수정
4 전자레인지 5  400000 <- 레코드 추가
전체 레코드 수 : 4


    [ 상품별 총금액 ]
냉장고 상품의 총금액은 1,700,000
세탁기 상품의 총금액은 1,650,000
HDTV 상품의 총금액은 6,000,000
전자레인지 상품의 총금액은 2,000,000
'''

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
    # db 연결 객체 생성 
    conn = pymysql.connect(**config)
    # SQL 실행 객체 생성
    cursor = conn.cursor()
    
    # goods 테이블 현황 
    print('\t[ goods 테이블 현황 ]')
    query = '''SELECT * FROM goods 
    '''
    cursor.execute(query)
    dataset = cursor.fetchall()
    for row in dataset:
        print('{0} {1} {2} {3:3,d}'.format(row[0],row[1],row[2],row[3]))
    print('전체 레코드수:',len(dataset))
    
    
    print('\t[ 상품별 총금액 ]')
    query1 = '''SELECT code, name, su*dan "tot" FROM goods 
    '''
    cursor.execute(query1)
    dataset1 = cursor.fetchall()
    for row in dataset1:
        print('{0} 상품의 총금액은 {1:3,d}'.format(row[1],row[2]))
    
    
except Exception as e :
    print('오류메세지: ',e)

finally:
    cursor.close() 
    conn.close() 

