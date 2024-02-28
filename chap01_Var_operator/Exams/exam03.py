'''
문3) 주어진 현재 온도와 습도를 대상으로 다음 3가지 질문에 대해서 답하시오.

    [질문1] 더운 날씨인가? -> 30도 이상이면 True, 미만이면 False  
    [질문2] 습한 날씨인가? -> 70 이상이면 True, 미만이면 False
    [질문3] 쾌적한 날씨인가? -> 30도 이상 이거나 습도가 70 이상이면 False
 '''
# 현재 온도 & 습도 
temp = 28 # 현재 온도 
hum = 80 # 현재 습도 

# 3가지 질문에 대한 응답 변수 : 내용 채우기 
is_hot = None
is_hum = None
is_comfortable = None

# 응답변수 출력 
print("더운 날씨인가?", is_hot)
print("습한 날씨인가?", is_hum)
print("쾌적한 날씨인가?", is_comfortable)


# 답 - 민정 
# 3가지 질문에 대한 응답 변수 : 내용 채우기 
is_hot = temp >= 30 #맞으면 True 반환
is_hum = hum >=70
is_comfortable = temp <30 and hum < 70 

# 응답변수 출력 
print("더운 날씨인가?", is_hot)
print("습한 날씨인가?", is_hum)
print("쾌적한 날씨인가?", is_comfortable)






