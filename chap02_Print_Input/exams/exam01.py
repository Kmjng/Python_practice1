﻿
'''
문1) 화씨를 키보드로 입력 받아서 섭씨로 변환하는 프로그램을 작성하시오.

   조건1> 화씨온도 변수명 : ftemp, 섭씨온도 변수명 : ctemp 
   조건2> 화씨온도는 키보드로 입력받는다.  
   조건3> 섭씨 온도변환 수식 = (화씨온도 - 32.0) * (5.0/9.0)
   조건4> 섭씨 온도 소숫점 3자리 표기  
   
   <<화면출력 결과>>
 화씨온도 : 93     -> 키보드 입력 
 섭씨온도 = 33.889
'''

# 1. 키보드 입력 
ftemp = int(input('화씨온도 : '))

# 2. 섭씨 온도 계산식
ctemp = (ftemp - 32.0) * (5/9)

# 3. 섭씨 온도 출력
print('섭씨온도 : {0:.3f} '.format(ctemp))

print('섭씨온도 : %.3f ' %(ctemp))

print(f'섭씨온도 : {ctemp} ') -- #이거는??????

print('섭씨온도 :' , format(ctemp, '.3f'))
