# class 정의

class TV :
    
    # 생성자 
    def __init__(self):
        # 멤버변수 초기화 
        self.power = False 
        self.channel = 10
        self.volume = 5     

    
    # 멤버메서드 
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
                  

    














 