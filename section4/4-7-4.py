import matplotlib.pyplot as plt

#리스트 범위(x축)
x = range(0, 256)

#리스트 범위(y축)
y = [v*v for v in x]

#테스트 출력
print(y)

#차트 설정1
plt.plot(x, y)

#차트 설정2
#plt.plot(x, y, 'ro')

#차트 실행
plt.show()
