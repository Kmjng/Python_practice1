
### 4. 문자열 처리 : 불용어 제거, 유효한 문자열 추출, 문자열 압축 


# [1] 중복 문자 제거하기 
'''
 예) "abcaabccde" -> "abcde"
'''
def remove_duplicates(string) :
    
    unique_chars = [] # 유일문자 저장 
    
    # 중복되지 않은 문자만 추가
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    
    # 중복 문자가 제거된 문자열 반환
    return ''.join(unique_chars)

# 테스트 입력
string = "abcaabccde"

print('result =', remove_duplicates(string))  # 출력: "abcd"


# [2] 유효한 괄호(대,중,소)로 묶은 문자열 추출하기 
'''
조건 : 괄호는 [], {}, () 이며 동일한 괄호는 중첩되지 않는다.
'''
def extract_valid_parentheses(string) :
    
    stack = [] # 문자 원소 저장 
    result = [] # 유효한 문자열 저장 
    mapping = {')': '(', '}': '{', ']': '['} 
    # 유효한 괄호 사전 : {key='닫기괄호': value='열기괄호'}
     
    for char in string : # 문자 단위 넘김 
        if char in mapping: # 문자열 key 조회  # 닫힌 괄호를 만나면 ★★★
            if stack[0] == mapping[char] : #mapping[char] 는 value # 첫번째요소(열린괄호)가 닫힌괄호랑 매칭되면~ 
                stack.append(char)             
                valid_str = ''.join(stack) 
                result.append(valid_str) # 매칭되면 저장하는 리스트 
                stack.clear() # stack 리스트는 임시로 사용하는 것이었음 
        else:
            stack.append(char) # '닫기괄호' 아닌 경우 stack 저장  
    
    return result

# 테스트 입력
string = "(abc){def}[ghi]"
result = extract_valid_parentheses(string)
print(result)  # 출력: ['[abc]', '{def}', '[ghi]']

string = "[abc](abc)"
result = extract_valid_parentheses(string)
print(result)  # 출력: ['[abc]', '(abc)']

string = "{def"
result = extract_valid_parentheses(string)
print(result)  # 출력: []



# [3] 문자열 압축 : 입력된 문자열을 순회하면서 '연속으로 반복'되는 문자들을 카운트하여 압축한 문자열 생성
'''
조건 : 문자열 압축 결과가 원래 문자열 보다 긴 경우 원래 문자열 반환
예) "aaaabbbcccc" -> "a4b3c4"   
'''

def compress_string(string):
    
    compressed = "" # 압축한 문자열 누적   
    count = 1 # 문자 카운트
    
    for i in range(1, len(string)):        
        if string[i] == string[i-1]: # 이전 문자와 같은 경우 
            count += 1 # 카운트 증가 
            
            if i == len(string)-1 : # 마지막 문자인 경우도 반드시 포함~~
                compressed += string[i-1] + str(count) # # 문자와 카운트값 결합 & 누적            
        else: # 다른 문자를 만난 경우 
            compressed += string[i-1] + str(count) # 문자와 카운트값 결합 & 누적 
            count = 1 # 카운트 초기화 
            
    return compressed 

# 테스트 입력
string = "aaabbbcccc"
print('result =', compress_string(string))  # result = a3b3c4

string = "abcd"
print('result =', compress_string(string))  # result = a1b1c1



# [문제] 주어진 문자열에서 반복되지 않는 첫번째 문자를 찾는 함수를 작성하시오.(없는 경우 None 반환)
'''
예1) "abcabcdeff" -> 출력결과 :  "d"
예2) "chatbot" -> 출력결과 :  "c"
예3) "botbot" -> 출력결과 : None   
'''

def find_first_unique_char(string):
    
    char_count = {} # 문자의 등장 횟수 저장 
    lst =[]
    # 1. 문자열을 순회하며 각 문자의 등장 횟수 카운트
    for i in string: 
        char_count[i] = char_count.get(i, 0) + 1 
    for j, k in char_count.items():
       if k == 1 :
           lst.append(j)
    if lst:
        return lst[0]
    else: 
        return None 
            
    
    # 2. 문자열을 순회하며 등장 횟수가 1인 첫번째 문자 반환 
        
   
    #return None   # 3. 반복되지 않는 문자가 없는 경우 None 반환 


# 테스트 자료 
print(find_first_unique_char("abaccdeff"))  # 출력: "b"
print(find_first_unique_char("chatbot"))    # 출력: "c"
print(find_first_unique_char("tbobot"))     # None
