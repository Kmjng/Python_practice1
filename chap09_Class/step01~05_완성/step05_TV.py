# class 정의

class TV :
    
    # 생성자 
    def __init__(self):
        print('~~ 생성자 ~~')
        # 동적 멤버변수 초기화 
        self.power = False # off/on
        self.channel = 10
        self.volume = 5     

    
    # 멤버메서드 : 리모콘  
    def changePower(self):
        self.power = not(self.power) 

    def volumeUp(self):
        self.volume += 1
        
    def volumeDown(self):
        self.volume -= 1        
       
    def channelUp(self):
        self.channel += 1 
        
    def channelDown(self):
        self.channel -= 1
                  

tv1 = TV() # 기본생성자 
 
dir(tv1)
   
tv1.changePower() # 전원 on
tv1.power # True

# volume : 5 -> 15
for i in range(10) :
    tv1.volumeUp()

tv1.volume # 15

# channel : 10 -> 5
for i in range(5) :
    tv1.channelDown()

tv1.channel # 5


tv2 = TV() # 생성자 

















 