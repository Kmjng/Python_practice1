# -*- coding: utf-8 -*-
"""
3. escape 문자 처리 
 escape 문자  : 특수기능의 문자(\n, \t, \b, \r, '', "")
                 \t : tap
                 \b : backspace
                 \r : return (carriage return)

"""

print('escape 문자')
# escape 기능 차단하는 두가지 방법
print('\\n출력') # escape 기능 차단1 - \ 
print(r'\n출력') # escape 기능 차단2 - r (raw의 약자)

# 경로 표현 
print('c:\python\test')
print('c:\\python\\test') 
print(r'c:\python\test')


# 문) c:\'aa'\"abc.txt" 형식으로 출력되도록 하시오.
print( ' c:\'aa\'\\"abc.txt" ') #문자열 안에있는 따옴표들이 빌런


file = open(r"C:\ITWILL\2_Python\test.txt", encoding='utf-8')
test= file.read()
print(test)

'''
사용된 함수 및 메소드 
open() 
read()
'''