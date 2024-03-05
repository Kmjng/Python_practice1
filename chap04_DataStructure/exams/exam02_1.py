'''
step02 문제
'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
print(message) # ['spam', 'ham', 'spam', 'ham', 'spam']

'''
문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      
  <출력결과>      
[1, 0, 1, 0, 1]
'''

dummy = [1 if i == 'spam' else 0 for i in message] # [내용 채우기]
print(dummy) # 출력결과 : [1, 0, 1, 0, 1]


'''
문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

spam_list = [i for i in message if i =='spam' ] # [내용 채우기]
print(spam_list) # 출력결과 : ['spam', 'spam', 'spam']










  