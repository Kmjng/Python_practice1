'''
문3) 다음과 같은 단계로 '서울' 지역을 대상으로 '동' 이름만 추출하여 출력하시오.
   단계1 : 'ooo동' 문자열 추출 : 예) '개포1동 경남아파트' -> '개포1동'
   단계2 : 중복되지 않은 전체 '동' 개수 출력 : 힌트) set 자료 이용
   단계3 : 중복되지 않은 서울시 전체 동 list 출력 
  
  <출력 예시>  
중복 포함 전체 동 개수 : 8080
서울시 전체 동 개수(중복제외) = 797

서울시 전체 동 list 출력   
['화양동', '풍납2동', '공릉동', '서울충정로우체국사서함', '도렴동', '교북동',
 '상봉2동', '홍제동', '염곡동', '체부동', '시흥4동', '홍제1동', '잠실3동', 
 '명일동', '묵정동', '신내동', '신설동', '번2동', '하왕십리동', '난곡동', '상계8동', '용문동', '양재2동', '홍지동', '갈현1동', '천호1동', '양평동', '수유3동', '목동', '돈암1동', '내수동', '목1동', '고척1동', '신영동', '대방동', '수유동'
'''


path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data'

file = open(path + "/zipcode.txt", mode='r', encoding='utf-8')
lines = file.readline() # 첫줄 읽는 객체 생성
dong = [] # '서울'의 동 저장 list

cnt =0 
while lines : #lines가 비어있으면 멈춤 
    tokens = lines.split(sep='\t') # tab 기준 : 토큰 생성 (리스트화)
    if tokens[1] =='서울':
    #if tokens[1].startswith('서울') :
        a = tokens[3].split(' ')
        dong.append(a[0]) 
        cnt +=1 
        
    lines = file.readline() # ★★★★ 그 다음 읽기를 꼭 해줘야 한다 ~~~~
    

print(dong, '\n중복 포함 서울시 총 동네수:',cnt)

file.close()
    
    
# 중복 제거 ( 어케하지 )

lines = file.readline() # 첫줄 읽는 객체 생성
dong = [] # '서울'의 동 저장 list

cnt =0 
while lines : #lines가 비어있으면 멈춤 
    tokens = lines.split(sep='\t') # tab 기준 : 토큰 생성 (리스트화)
    if tokens[1] =='서울':
    #if tokens[1].startswith('서울') :
        if tokens[3] not in dong:
            a = tokens[3].split(' ')
            dong.append(a[0]) 
            cnt +=1  
    lines = file.readline()
    

print(dong, '\n총 동네수:',cnt)

file.close()    


# 중복제거 set() 이용 

dong2 = list(set(dong))
print(dong2, '\n중복 미포함 서울시 총 동네수:',len(dong2))
file.close()    
    

    
    
    




    