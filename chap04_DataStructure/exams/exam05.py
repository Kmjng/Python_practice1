'''
step05 문제

 문3) 다음 movie 객체를 대상으로 평점 8이상인 영화 제목과 전체 누적관객수를 출력하시오.

 <출력 결과>
 영화제목 : 광해
 영화제목 : 관상
 누적 관객수 =  2,100
'''

movie = {'광해' : [9.24, 1200], '공작' : [7.86, 500], '관상' : [8.01, 900]}

tot_info ={}
tot =0
for i, j in movie.items():
    if j[0]>=8:
        print(f"영화제목: {i}")
        tot += j[1]
print(f'누적 관객수 = {tot}')