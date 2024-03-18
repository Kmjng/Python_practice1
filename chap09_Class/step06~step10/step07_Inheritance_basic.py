'''
클래스 상속( Inheritance )
 - 기존 클래스(부모)를 이용하여 새로운 클래스(자식) 작성 기법 
 - 목적 : 클래스 설계 시 가이드라인을 제시하는 역할
 - 상속 대상 : 부모클래스 멤버(멤버변수+멤버메서드)   
 - 생성자(__init__())는 상속 대상이 아님!!! (그냥 호출)
 형식)
 class 자식클래스(부모클래스) :
     클래스 본체
'''
     

# 동물 클래스 
class Animal: # '이름'과 '울음소리' 만 저장
    def __init__(self, name): #생성자
        self.name = name # 맴버변수

    def speak(self): # 맴버메서드
        pass
    def meal(self):
        print(f"{self.name}의 밥은 사료입니다.")

class Dog(Animal): # 자식클래스1
    def speak(self): #메소드 재정의 (오버라이딩★★★)
        print(f"{self.name}가 짖습니다.")

class Cat(Animal): # 자식클래스2
    def speak(self):
        print(f"{self.name}가 야옹합니다.")

'''
자식 클래스는 부모 클래스의 기능을 상속받지만, 
때로는 부모 클래스의 메서드를 그대로 사용하기보다는 
자식 클래스의 특정한 요구에 맞게 기능을 확장하거나 변경해야 할 때가 있다.
이를 위해 부모 클래스의 메서드를 자식 클래스에서 재정의하여 새로운 동작을 구현할 수 있다.
'''

# 자식클래스는 생성자__init__가 없음
dog1 = Dog('푸들')
dir(dog1)
'''
.... 'name',
 'speak']
''' 
dog1.name # >> 푸들
dog1.speak()  # >> 푸들가 짖습니다. 


dog1.meal()  # >> 푸들의 밥은 사료입니다. #부모클래스 맴버 사용







