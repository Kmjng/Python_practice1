'''

문4) tot 함수를 인수로 받아서 dataset 각 원소의 합을 계산하는 함수를 완성하시오.

  <출력 결과>
  tot = [12.5, 7, 22.3]
'''
# dataset
datas = [[2,4.5,6], [3,4], [5,8.3,9]]
# tot 함수 정의 
def tot(x): 
    return sum(x)
# tot 함수를 인수로 받는 함수 정의 
def my_func(func,datas):
    lst = [func(i) for i in datas]
    return lst 

print(my_func(tot, datas))

