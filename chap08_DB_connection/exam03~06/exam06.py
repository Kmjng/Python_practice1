# -*- coding: utf-8 -*-
"""        
문제6) 부서별 급여 평균을 계산하여 평균이 200 이상인 부서만 아래와 같은 
     출력양식으로 출력하시오.     
     사용 테이블 : emp_test   
    
    
	<<평균 급여 200 이상 부서>>
부서번호  급여합계   급여평균
    10      500     250.00
    20      700     350.00
전체 레코드 수 : 2
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
    query = f"""SELECT dno, SUM(sal), AVG(sal) FROM emp_test
    GROUP BY dno
    """
    cursor.execute(query)
    dataset= cursor.fetchall()
    print("<<평균 급여 200 이상인 부서>>\n")
    print("부서번호\t급여합계\t급여평균")
    for row in dataset:
        print("{}\t{}\t{}".format(row[0],row[1],row[2]))
    print("전체 레코드 수 :",len(dataset))
            
except Exception as e :
    print('db error : ', e)
finally :
    cursor.close(); conn.close()