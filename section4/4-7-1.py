from pandas import Series
#matplotlib, pandas_datareader

#Series1 선언
series1 = Series([92600, 92400, 92100, 94300, 92300])
#출력
print(series1)
#총 개수
print('count',series1.count())
#요약
print('count',series1.describe())
#인덱스 접근
print(series1[0])

#Series2 선언
series2 = Series([92600, 92400, 92100, 94300, 92300], index=['2018-02-19','2018-02-18','2018-02-17','2018-02-16','2018-02-15'])
#출력2
print(series2)

#인덱스 순회
for date in series2.index:
    print('date',date)

#값 순회
for price in series2.values:
    print('price',price)

#Series3 선언
series_g1 = Series([10, 20, 30], index=['n1', 'n2', 'n3'])
series_g2 = Series([10, 30, 20], index=['n2', 'n1', 'n3'])

#Series 병합 & 계산
sum = series_g1 + series_g2
mul = series_g1 * series_g2
cul = (series_g1 * series_g2) * 0.5

#출력
print('sum')
print(sum)
print('mul')
print(mul)
print('cul')
print(cul)
