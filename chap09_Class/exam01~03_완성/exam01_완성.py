'''
 문1) 다음 처리조건에 맞게 Rectangle 클래스를 정의하시오.

 <처리조건>
 1. 멤버 변수 : 가로(width), 세로(height)
 2. 생성자 : 가로(width), 세로(height) 멤버 변수 초기화
 3. 멤버 메서드(area_calc) : 사각형의 넓이를 구하는 메서드
          사각형 넓이 = 가로 * 세로 
 4. 멤버 메서드(circum_calc) : 사각형의 둘레를 구하는 메서드
          사각형 둘레 = (가로 + 세로) * 2
 5. 기타 출력 예시 참조
   
       << 출력 예시 >>       
    사각형의 넓이와 둘레를 계산합니다.
    사각형의 가로 입력 : 10
    사각형의 세로 입력 : 5
    ----------------------------------------
    사각형의 넓이 : 50
    사각형의 둘레 : 30
    ----------------------------------------
'''

class Rectangle :    
    # 멤버변수 : 가로, 세로 
    width = height = 0

    # 생성자 : 객체 생성 & 멤버변수 초기화 
    def __init__(self, width, height) :
        # 멤버변수 초기화 
        self.width = width
        self.height = height
   
    # 멤버메서드 : 넓이 계산
    def area_calc(self):
        area = self.width * self.height # 가로 * 세로
        print('사각형의 넓이 :',area)
    
    # 멤버메서드 : 둘레 계산
    def circum_calc(self):
        circum = (self.width + self.height) * 2 # (가로 + 세로) * 2
        print('사각형의 둘레 :', circum)
    


# 키보드 입력 
print("사각형의 넓이와 둘레를 계산합니다.")
w = int(input('사각형의 가로 입력 : ')) # 10
h = int(input('사각형의 세로 입력 : ')) # 5

# 객체 생성 
rect = Rectangle(w, h) # 생성자(실인수) 

dir(rect)
'''
 'area_calc',
 'circum_calc',
 'height', = 10
 'width'] = 5
'''    

print('-'*30)
# 사각형 넓이 계산 
rect.area_calc()

# 사각형 둘레 계산 
rect.circum_calc()
print('-'*30)

# 두번째 객체 
rect2 = Rectangle(20, 10)

dir(rect2)
'''
 'area_calc',
 'circum_calc',
 'height',
 'width']
'''    

rect2.area_calc() # 사각형의 넓이 : 200
rect2.circum_calc() # 사각형의 둘레 : 60

# 객체 출처(class) 
print(type(rect)) # <class '__main__.Rectangle'>
print(type(rect2)) # <class '__main__.Rectangle'>


















