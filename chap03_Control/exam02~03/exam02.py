'''
step02 관련 문제

문) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기를 구현하시오.
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''

print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)



# 민정 
coffee = 3 # 커피 3잔

while True: # 무한 반복
    pass  # ★★★
    # 밑에 if에 선택되고 수행한 다음 while True에 의해 
    if coffee == 0: # 종료 조건
        print('이제 장사 종료')
        break
    elif coffee == 3 or coffee !=3 : # 세잔 또는 몇 잔 남아있으면
        put = int(input('투입 금액: ')) # ★★★
        if put < 2500 : 
            print('금액이 부족합니다.')
            continue 
        elif put > 2500:
            print('맛있게 드세요.\n잔돈:{}'.format(put-2500))
            coffee -= 1 
            print('남은 커피 수:{}'.format(coffee))
        else: 
            print('맛있게 드세요.')
            coffee -= 1 
            print('남은 커피 수:{}'.format(coffee))
            
    
# 정답 
coffee = 3 # 커피 3잔

while True: # 무한 반복
    put = int(input('투입 금액: '))
    if put < 2500 : 
        print('금액이 부족합니다.')
        continue 
    elif put > 2500:
        print('맛있게 드세요.\n잔돈:{}'.format(put-2500))
        coffee -= 1 
        print('남은 커피 수:{}'.format(coffee))
    else: 
        print('맛있게 드세요.')
        coffee -= 1 
        print('남은 커피 수:{}'.format(coffee))
    if coffee == 0: # ★★★ 종료 조건
        print('남은 수량이 없습니다.')
        break
    





