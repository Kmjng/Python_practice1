DROP TABLE student; -- 테이블 삭제 

CREATE or REPLACE TABLE student( 
  studno int primary key,              
  sname varchar(10) not null,                        
  tel varchar(15),     
  deptno int,                
  profno  int                
); 

SELECT * FROM student;

COMMIT;