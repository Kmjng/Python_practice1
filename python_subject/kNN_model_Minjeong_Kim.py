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

'''
# 단계2. kNN 분류기(클래스 정의) : 데이터(필드) + 알고리즘(메서드)
class kNN :    
    def __init__(self, q, p):
        self.q = q 
        self.p = p 
    def distances(self):
        self.dist = [] 
        for i in range(len(q)):
            
            self.x1 = (q[i][0]-p[0])**2
            self.y1 = (q[i][1]-p[1])**2
            self.d1 = (self.x1+self.y1)**(1/2)
            self.dist.append(self.d1)
            self.dist=sorted(self.dist, reverse=False)
            
        return self.dist
    def axis(self):
        return q    
    def k(self,j): #최근접 이웃 j개 거리 추출 메소드
        return self.dist[:j]
''' 
# 단계2. kNN 분류기(클래스 정의) : 데이터(필드) + 알고리즘(메서드)
class kNN :    
    def __init__(self, q, p):
        self.q = q 
        self.p = p 
    def distances(self):
        
        self.real = {}
        self.dist =[]
        for i in range(len(q)):
        
            self.x1 = (q[i][0]-p[0])**2
            self.y1 = (q[i][1]-p[1])**2
            self.d1 = (self.x1+self.y1)**(1/2)
            self.real[i]= self.d1 # {0:~~} # 딕셔너리에 순서 저장하고 
            self.dist.append(self.d1) # 리스트에 거리 저장 
            self.dist = sorted(self.dist, reverse=False) #value로 정렬
            
        return self.dist
    
    def k(self,j): #최근접 이웃 j개 거리 추출 메소드
        real_d = []
        self.dist2 = sorted(self.dist, key = self.dist.get, reverse=False) # key 반환 
        
        for i in self.dist2[:j]: #[1,7,3]
            real_d.append(q[i])
        return self.dist3, real



# 단계3. kNN 객체 생성             
knn = kNN(q, p) # (적용데이터셋, 기준데이터셋)
knn.distances()
knn.k(3)

print(f'k1 ->{knn.k(1)}')
print(f'k3 ->{knn.k(3)}')
print(f'k5 ->{knn.k(5)}')


    


