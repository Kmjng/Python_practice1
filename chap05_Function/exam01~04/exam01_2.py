'''
step01

문2) 각 층 단위로 별(Start) 출력 및 별의 총 개수 구하기   


<출력 예시>
층수(height) 입력 : 5 
*
**
***
****
*****
별(start) 개수 : 15 
'''

# 함수 정의
def StarCount(height):  
    # 층 개수, 별 개수 변수 선언 
    h_cnt = s_cnt = 0
    for i in range(height): # 주의: 'int' object is not iterable
        h_cnt += 1
        print( "*"*h_cnt )
        s_cnt += h_cnt
    
    
    return s_cnt




# 키보드 입력 & 함수 호출
star_cnt = StarCount(int(input('층수(height) 입력 : '))) # 층 수 입력

# start 개수 출력
print('별(start) 개수 : %d'%star_cnt)

