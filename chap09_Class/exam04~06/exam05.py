'''
문5) 도형(Shape) 클래스는 모든 도형의 면적(area)를 구하는 메서드로 정의되어 있습니다.
     이 메서드를 상속받아서 원의 넓이(면적)과 사각형의 넓이(면적)을 구하는 수식으로 
     재정의하시오. <출력 결과 예시> 참고 
     
     원의 넓이 수식 = 반지름(radius) * 반지름(radius) * 3.14  
     사각형의 넓이 수식 = 가로 * 세로    
     
    <출력 결과 예시>
     반지름 = 5 -> 원의 넓이 = 78.5
     가로 = 4, 세로 = 6 -> 사각형의 넓이 = 24 
'''

# 도형 클래스 
class Shape():
    def area(self):
        pass

# 원 클래스 
class Circle(Shape):
    
    # 생성자 
    def __init__(self, radius): # 인수 : 반지름 
        self.radius = radius
    def area(self):
        self.area = 3.14*(self.radius **2)
        print("반지름 ={0} -> 원의 넓이 ={1}".format(self.radius, self.area))
    

# 사각형 클래스 
class Rectangle(Shape):
    
    # 생성자  
    def __init__(self, width, height): # 인수 : 가로, 세로 
        self.width = width
        self.height = height
    
    def area(self):
        self.area = self.width * self.height
        print("가로 ={0}, 세로={1} -> 원의 넓이 ={2}".format(self.width, self.height, self.area))
    
# 객체 생성  
my_circle = Circle(5) # 반지름=5
my_rectangle = Rectangle(4, 6) # 가로=4, 세로=6
my_circle.area()
my_rectangle.area()














