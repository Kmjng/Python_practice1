# -*- coding: utf-8 -*-
"""
클래스 과제 : kNN 알고리즘 구현 
"""

import random # 난수 생성 모듈 
# from statistics import sqrt # 제곱근 함수 

random.seed(100) # 난수 seed값 지정(난수 고정) 

### 단계1. data 생성 

# 1) 적용데이터셋 10개  : 소숫점 5자리 반올림 
q = [[round(random.random(), 5), round(random.random(), 5)] for i in range(10)]

# 2) 기준데이터셋 1개 : 소숫점 5자리 반올림
p = [round(random.random(), 5), round(random.random(), 5)]

print('q :', q)
print('p : ', p)
print('-'*60)


# 단계2. kNN 분류기(클래스 정의) : 데이터(필드) + 알고리즘(메서드)
class kNN :    
    def __init__(self, q, p):
        self.q = q 
        self.p = p 
        
        
    def distances(self, j):
        self.real = {}  # q 좌표들과 p까지의 거리를 매칭하기 위한 딕셔너리
        self.dist =[]
        for i in range(len(q)):
        
            self.x1 = (self.q[i][0]-self.p[0])**2
            self.y1 = (self.q[i][1]-self.p[1])**2
            self.d1 = (self.x1+self.y1)**(1/2)

            self.real[i]= self.d1 # {0:~~} # 딕셔너리에 q 좌표순서 저장 
            self.dist.append(self.d1) # 리스트에 '거리' 저장 
            self.dist = sorted(self.dist, reverse=False) #value로 정렬
            
        return self.dist[:j] #  j 까지의 최근접거리 반환
    
    def k(self,j): #최근접 이웃 j개 거리좌표 추출 메소드
        self.real_d = [] # 좌표 담을 리스트
        self.real_sorted = sorted(self.real, key = self.real.get, reverse=False) # key 반환 
        for i in self.real_sorted[:j]: #[1,7,3]
            self.real_d.append(self.q[i])
        return self.real_d



# 단계3. kNN 객체 생성             
knn = kNN(q, p) # (적용데이터셋, 기준데이터셋)
knn.distances(3)
knn.k(3)
print(knn.k(1))
print('k1 ->{0}\nreal data: {1}'.format(knn.distances(1),knn.k(1)))
print('k3 ->{0}\nreal data: {1}'.format(knn.distances(3),knn.k(3)))
print('k5 ->{0}\nreal data: {1}'.format(knn.distances(5),knn.k(5)))


    


