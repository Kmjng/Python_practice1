'''
문제2) emp01 테이블을 이용하여 다음과 같은 형식으로 출력하시오.  
      <조건> 사번 : 오른쪽 기준 (정렬), 문자 : 왼쪽 기준, 급여 : 천단위 콤마 
 
 <출력결과>     
 ---------------------------------
 empno   ename   job	      sal
 ---------------------------------
  7369  SMITH   CLERK       800
  7499  ALLEN   SALESMAN    1,600
  7521  WARD    SALESMAN    1,250
  7566  JONES   MANAGER     2,975
  7654  MARTIN  SALESMAN    1,250
  7698  BLAKE   MANAGER     2,850
  7782  CLARK   MANAGER     2,450
  7788  SCOTT   ANALYST     3,000
  7839  KING    PRESIDENT   5,000
  7844  TURNER  SALESMAN    1,500
  7876  ADAMS   CLERK       1,100
  7900  JAMES   CLERK       950
  7902  FORD    ANALYST     3,000
  7934  MILLER  CLERK       1,300
 ---------------------------------
 전체 레코드 수 : 14
 ---------------------------------
'''


# 조회하는 문제
import oracledb

try :
    conn = oracledb.connect(dsn='127.0.0.1:1521/XE', 
                            user='c##scott',
                            password='tiger') #연결객체
    cursor = conn.cursor() # 커서객체(실행객체)
    
    query = """SELECT empno,ename,job, sal FROM emp01
    """
    cursor.execute(query) # 커서객체를 통해 쿼리 실행(execute)
    dataset = cursor.fetchall() # 리스트 객체 생성
    print('-'*40)
    print('empno\tename\tjob\t\t\tsale\t')
    print('-'*40)
    for row in dataset: 
        print('{0:<8} {1:<10} {2:<10} {3:3,d}'.format(row[0],row[1],row[2],row[3]))
    print('-'*40)
    print('레코드 수 :',len(dataset))
except Exception as e :
    print('오류 메세지 :',e)

finally:
    cursor.close()
    conn.close() 


'''
오류 메세지 : unsupported format string passed to NoneType.__format__
>> 데이터를 인덱스에 할당하는데 null 값이 있으면 나타나는 오류 인듯 
'''

# 해결방법 
'''
if row[3] is not None:
            print('{0:<8} {1:<10} {2:<10} {3:3,d}'.format(row[0], row[1], row[2], row[3]))
        else:
            print('{0:<8} {1:<10} {2:<10} {3}'.format(row[0], row[1], row[2], 'null'))
'''
