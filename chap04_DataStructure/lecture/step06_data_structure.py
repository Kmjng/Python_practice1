# -*- coding: utf-8 -*-
"""
데이터 구조화의 예 : 제품구매 정보 관리 
 - 자료를 효율적으로 관리하고 처리(추가, 수정, 삭제)가 용이하다.
"""

# 데이터 구조화 예 : 제품구매 정보 관리
purchase_list = [
    {"제품명": "사과", "가격": 1000, "수량": 5, "총액": 5000}, # 1행 
    {"제품명": "바나나", "가격": 1500, "수량": 3, "총액": 4500}, # 2행 
    {"제품명": "딸기", "가격": 2000, "수량": 2, "총액": 4000} # 3행 
] # 행과 열의 테이블 구조  
# 요소(행) 안에 있는 열들은 순서가 없는 상태로 저장됨 (아마도)


print(purchase_list)

# 1. 구매 제품 양식 출력  
for purchase in purchase_list:
    print(f"{purchase['제품명']} - 가격: {purchase['가격']}원, 수량: {purchase['수량']}, 총액: {purchase['총액']}원")
    
    
# 2. 새 구매제품 추가 : "오렌지", 1200, 4
product_name = "오렌지"
price = 1200
quantity = 4    
total_price = price * quantity

new_purchase = {"제품명": product_name, "가격": price, "수량": quantity, "총액": total_price}
purchase_list.append(new_purchase)

for purchase in purchase_list:
    print(f"{purchase['제품명']} - 가격: {purchase['가격']}원, 수량: {purchase['수량']}, 총액: {purchase['총액']}원")


# 3. 구매제품 수정 : 오렌지 제품 단가, 수량 수정 
product_name = "오렌지"
price = 1500
quantity = 8    

for purchase in purchase_list:
    if purchase['제품명'] == product_name :
        purchase['가격'] = price
        purchase['수량'] = quantity
        purchase['총액'] = price * quantity
