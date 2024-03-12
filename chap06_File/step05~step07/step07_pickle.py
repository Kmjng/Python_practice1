'''
pickle 파일 
 - 파이썬 객체(list, dict)를 이진파일(binary)로 저장
 
이진파일로 작업하면 처리 속도가 빨라진다. 
 
'''
lst = [1,2,3,4,5]
type(lst)

path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data' 

file = open(path +'\list_data.txt', mode = 'w')
file.write(lst) # TypeError: write() argument must be str, not list
# write() : 파일 쓰기 기능. str타입을 받는다. ★★★
file.write(str(lst)) #
file.close()

# 1. file read 
path = r'C:/ITWILL/2_Python/workspace/Python_practice1/chap06_File/data' 

file = open(path + '/texts.txt', mode = 'r', encoding='utf-8')

file2 = open(path+'\list_data.txt', mode='r')

text = file2.read() # str형 객체 
print(text, type(text)) # [1, 2, 3, 4, 5] <class 'str'>
print(text[0]) # >> '['
file2.close() 

texts = file.readlines() # list 반환
texts # list형 
texts[-1] # '나는 홍길동' list마지막 요소 반환 



# 2. word 추출  
words = []

for line in texts : # list
    for word in line.split() : 
        words.append(word)
        
print(words)
   

# 3. pickle save & load 

import pickle 

# binary file save
file = open(path + '/wc_data.pickle', mode='wb') # +binary ★★★★★★
pickle.dump(words, file) 
file.close()


# load
file = open(path+'/wc_data.pickle', mode='rb') 
wc_data = pickle.load(file) # load(file)  #load 할때에는 객체에 담아야 한다. (사용법임)

print(type(wc_data))
print(wc_data)
file.close()










